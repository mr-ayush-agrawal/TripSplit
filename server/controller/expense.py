import secrets
from datetime import datetime
from server.utils.logger import logging
from server.models.expense import NewExpense, Expense, UpdateExpense
from fastapi import HTTPException
from server.databases.config import database

expense_collection = database.get_expense_collection()
group_collection = database.get_group_collection()


def add_expense(group_id : str, expense: NewExpense, current_user : str):
    try : 
        group = group_collection.find_one({'group_id': group_id})
        if not group:
            logging.error(f'No group found wiht id {group_id}')
            raise HTTPException(status_code=404, detail="Group not found")
        
        if current_user['user_name'] not in group['members']:
            logging.error(f'User {current_user['user_name']} not in group {group_id}')
            raise HTTPException(status_code=403, detail="User not in the group")


        logging.info(f'Adding expense to the group')
        expense_id = create_unique_expense_id()
        new_exp = Expense(
            **expense.model_dump(),
            expense_id=expense_id,
            group_id=group_id,
            expense_owner=current_user['user_name']
        )

        expense_collection.insert_one(new_exp.model_dump())
        total_expense_increment = new_exp.amount
        updated_balances = group.get('member_balances', {})
        for user, amount in new_exp.paid_by.items():
            updated_balances[user] = updated_balances.get(user, 0.0) + amount
        for user, amount in new_exp.borrowed_by.items():
            updated_balances[user] = updated_balances.get(user, 0.0) - amount
        updated_balances = {k: round(v, 2) for k, v in updated_balances.items()}


        group_collection.update_one(
            {"group_id": group_id},
            {
                "$push": {"expenses": expense_id},
                "$set": {"member_balances": updated_balances},
                "$inc": {"total_expense": total_expense_increment}
            }
        )
        
        logging.info(f'Expense added successfully {expense_id}')
        return {
            "status_code": 200,
            "message": "Expense added successfully",
            "expense_id" : expense_id,
            "data": new_exp
        }

    except Exception as e:
        logging.error(f'Failed to add expense: {str(e)}')
        return {
            'status_code': 500,
            'message': f'Internal server error: {str(e)}'
        }
    
def all_expenses(group_id: str, current_user: str):
    try : 
        logging.info(f'Fetching all expenses for group {group_id}')

        group = group_collection.find_one({'group_id': group_id})
        if not group:
            logging.error(f'No group found with id {group_id}')
            raise HTTPException(status_code=404, detail="Group not found")
        
        if current_user['user_name'] not in group['members']:
            logging.error(f'User {current_user["user_name"]} not in group {group_id}')
            raise HTTPException(status_code=403, detail="User not in the group")

        expenses = list(expense_collection.find({'group_id': group_id}))
        username = current_user['user_name']
        user_expense_summary = []
        total_paid = 0.0
        total_borrowed = 0.0

        for exp in expenses:
            paid_by = exp["paid_by"].get(username, 0.0)
            borrowed_by = exp["borrowed_by"].get(username, 0.0)
            total_paid += paid_by
            total_borrowed += borrowed_by

            paid_by_orig = exp["paid_by_original"].get(username, 0.0)
            borrowed_by_orig = exp["borrowed_by_original"].get(username, 0.0)

            date = exp.get("date") or exp.get("created_at")
            if isinstance(date, datetime):
                date = date.isoformat()
            user_expense_summary.append({
                "expense_id" : exp["expense_id"],
                "title": exp["title"],
                "description": exp.get("description"),
                "amount": exp["amount_original"],  # in original currency
                "currency": exp['original_currency'],
                "paid_by_user": paid_by_orig,
                "borrowed_by_user": borrowed_by_orig,
                "date": date
            })
        
        net_amount = round(total_paid - total_borrowed, 2)

        logging.info(f"All expenses fetched for {group_id}")
        
        return {
            "status_code": 200,
            "message": "Expenses fetched successfully",
            "data": {
                "group_name": group['group_name'],
                "amount": net_amount,
                "currency": group['base_currency'],
                "expenses": user_expense_summary
            }
        }
    except Exception as e :
        logging.error(f'Failed to fetch the expenses for the group {group_id}')
        raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

def single_expense(group_id: str, expense_id: str, current_user: str):
    try: 
        logging.info(f'Fetching expense {expense_id} for group {group_id}')

        group = group_collection.find_one({'group_id': group_id})
        if not group:
            logging.error(f'No group found with id {group_id}')
            raise HTTPException(status_code=404, detail="Group not found")
        if current_user['user_name'] not in group['members']:
            logging.error(f'User {current_user["user_name"]} not in group {group_id}')
            raise HTTPException(status_code=403, detail="You are not a member of this group")

        expense = expense_collection.find_one({'expense_id': expense_id, 'group_id': group_id})
        if not expense:
            logging.error(f'No expense found with id {expense_id} in group {group_id}')
            raise HTTPException(status_code=404, detail="Expense not found")
        
        user_amount = expense.get('paid_by_original', {}).get(current_user['user_name'], 0.0) - expense.get('borrowed_by_original', {}).get(current_user['user_name'], 0.0)

        expense.pop('_id', None)
        logging.info(f"Details fetched for expense {expense_id}")
        return {
            "status_code": 200,
            'user_amount' : user_amount, 
            "expense": expense
        }
        
    except Exception as e:
        logging.error(f'Failed to fetch expense {expense_id} for group {group_id}: {str(e)}')
        raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

def update_expense(group_id: str, expense_id : str, updated_data : UpdateExpense, current_user):
    try:
        group = group_collection.find_one({"group_id": group_id})
        if not group :
            raise HTTPException(status_code=404, detail="Group not found")
        if current_user['user_name'] not in group['members']:
            raise HTTPException(status_code=403, detail="User not in group")
        existing_exp = expense_collection.find_one({"expense_id": expense_id, 'group_id': group_id})

        if not existing_exp:
            raise HTTPException(status_code=404, detail="Expense not found")
        if existing_exp["expense_owner"] != current_user["user_name"]:
            raise HTTPException(status_code=403, detail="Only the expense owner can edit the expense")
        
        update_fields = {k: v for k, v in updated_data.model_dump().items() if v is not None}

        if not update_fields:
            raise HTTPException(status_code=400, detail="No update fields provided")
        
        merged_data = existing_exp.copy()
        merged_data.update(update_fields)

        recalculate_balances = any(
            field in update_fields for field in ["paid_by_original", "borrowed_by_original", "exchange_rate"]
        )

        updated_balances = group.get("member_balances", {})

        if recalculate_balances:
            # Revert old balances
            for user, amt in existing_exp["paid_by"].items():
                updated_balances[user] = updated_balances.get(user, 0.0) - amt
            for user, amt in existing_exp["borrowed_by"].items():
                updated_balances[user] = updated_balances.get(user, 0.0) + amt

        # Validate final merged data
        updated_exp = Expense(**merged_data)
        

        if recalculate_balances:
            for user, amt in updated_exp.paid_by.items():
                updated_balances[user] = updated_balances.get(user, 0.0) + amt
            for user, amt in updated_exp.borrowed_by.items():
                updated_balances[user] = updated_balances.get(user, 0.0) - amt
            updated_balances = {k: round(v, 2) for k, v in updated_balances.items()}

        # Update the expense
        expense_collection.update_one(
            {"expense_id": expense_id},
            {"$set": updated_exp.model_dump()}
        )

        # Update balances only if changed
        if recalculate_balances:
            group_collection.update_one(
                {"group_id": group_id},
                {"$set": {"member_balances": updated_balances}}
            )

        logging.info(f"Updated the expense {expense_id}")
        return {
            "status_code": 200,
            "message": "Expense updated successfully",
            "expense_id": expense_id,
            "data": updated_exp
        }
        
    except Exception as e:
        logging.error(f'Failed to update expense {expense_id} for group {group_id}: {str(e)}')
        raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')

def delete_single_expense(group_id: str, expense_id: str, current_user: dict):
    try :
        group = group_collection.find_one({"group_id": group_id})
        if not group:
            raise HTTPException(status_code=404, detail="Group not found")
        if current_user['user_name'] not in group['members']:
            raise HTTPException(status_code=403, detail="User not in the group")

        expense = expense_collection.find_one({"expense_id": expense_id, "group_id": group_id})
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        
        is_owner = expense["expense_owner"] == current_user["user_name"]
        is_admin = current_user["user_name"] == group.get("owner_username")
        if not (is_owner or is_admin):
            raise HTTPException(status_code=403, detail="Only the expense owner or group admin can delete this expense")

        updated_balances = group.get("member_balances", {})
        for user, amt in expense["paid_by"].items():
            updated_balances[user] = updated_balances.get(user, 0.0) - amt
        for user, amt in expense["borrowed_by"].items():
            updated_balances[user] = updated_balances.get(user, 0.0) + amt
        updated_balances = {k: round(v, 2) for k, v in updated_balances.items()}

        expense_collection.delete_one({"expense_id": expense_id})
        group_collection.update_one(
            {"group_id": group_id},
            {
                "$pull": {"expenses": expense_id},
                "$set": {"member_balances": updated_balances},
                "$inc": {"total_expense": -expense["amount"]}
            }
        )
        
        logging.info(f'Expense {expense_id} Deleted succecsfully')
        return {
            "status_code": 200,
            "message": "Expense deleted successfully",
            "expense_id": expense_id
        }

    except Exception as e:
        logging.error(f"Error deleting expense: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

def create_unique_expense_id():
    i = 0
    while i<100:
        exp_id = secrets.token_hex(5)
        exists = group_collection.find_one({"expense_id": exp_id})
        if not exists:
            return exp_id
        i+=1
    logging.error('Failed to generate unique group ID after 100 attempts')
    raise HTTPException(
        status_code=500,
        detail='Failed to generate unique group ID'
    )    