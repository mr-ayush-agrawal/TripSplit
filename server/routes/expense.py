from fastapi import APIRouter, Depends, HTTPException
from server.models.expense import NewExpense, Expense

from server.middleware.auth import is_logged_in

from server.controller.expense import (
    all_expenses, add_expense, single_expense
)

expense_router = APIRouter(tags=["Expenses"])

@expense_router.get('/')
async def all_group_expenses(group_id:str, current_user = Depends(is_logged_in)):
    return all_expenses(group_id, current_user)

@expense_router.get('/expense/{expense_id}')
async def get_expense_by_id(group_id: str, expense_id: str, current_user = Depends(is_logged_in)):
    return single_expense(group_id, expense_id, current_user)

@expense_router.post('/add-expense')
async def add__new_expense(group_id : str, expense: NewExpense, current_user = Depends(is_logged_in)):
    return add_expense(group_id, expense, current_user)




