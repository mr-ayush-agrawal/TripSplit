import secrets
from datetime import datetime
from server.utils.logger import logging
from server.models.expense import NewExpense, Expense
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
        return {
            "status_code": 200,
            'user_amount' : user_amount, 
            "expense": expense
        }
        
    except Exception as e:
        logging.error(f'Failed to fetch expense {expense_id} for group {group_id}: {str(e)}')
        raise HTTPException(status_code=500, detail=f'Internal server error: {str(e)}')


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