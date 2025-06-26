from fastapi import APIRouter, Depends
from server.models.expense import NewExpense, UpdateExpense

from server.middleware.auth import is_logged_in
from server.controller.expense import *

expense_router = APIRouter(tags=["Expenses"])

@expense_router.get('/')
async def all_group_expenses(group_id:str, current_user = Depends(is_logged_in)):
    return all_expenses(group_id, current_user)

@expense_router.get('/{expense_id}')
async def get_expense_by_id(group_id: str, expense_id: str, current_user = Depends(is_logged_in)):
    return single_expense(group_id, expense_id, current_user)

@expense_router.post('/add-expense')
async def add_new_expense(group_id : str, expense: NewExpense, current_user = Depends(is_logged_in)):
    return add_expense(group_id, expense, current_user)

@expense_router.patch('/{expense_id}/update-expense')
async def update_existing_expense(group_id: str, expense_id : str, expense : UpdateExpense, current_user = Depends(is_logged_in)):
    return update_expense(group_id, expense_id, expense, current_user)

@expense_router.delete('/{expense_id}/delete')
async def delete_expense_by_id(group_id : str, expense_id : str, current_user = Depends(is_logged_in)):
    return delete_single_expense(group_id, expense_id, current_user)
