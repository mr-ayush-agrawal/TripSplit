import secrets
from fastapi import APIRouter, Depends, HTTPException
from server.models.expense import NewExpense, Expense
from server.databases.config import database
from server.middleware.auth import is_logged_in

from server.utils.logger import logging

expense_router = APIRouter(tags=["Expenses"])
expense_collection = database.get_expense_collection()
group_collection = database.get_group_collection()

@expense_router.get('/')
async def test(group_id:str, current_user = Depends(is_logged_in)):
    return{
        'status_code': 200,
        'data' : {
            'group_id' : group_id, 
            'user_name' : current_user['user_name']
        }
    }

@expense_router.post('/add-expense')
async def add_expense(group_id : str, expense: NewExpense, current_user = Depends(is_logged_in)):
    print('Called')
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
        
        # Updating the group with the expesne
        group_collection.update_one(
            {"group_id": group_id},
            {
                "$push": {"expenses": expense_id}
            }
        )

        return {
            "status_code": 200,
            "message": "Expense added successfully",
            "data": new_exp
        }

    except Exception as e:
        logging.error(f'Failed to add expense: {str(e)}')
        return {
            'status_code': 500,
            'message': f'Internal server error: {str(e)}'
        }
    




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
    