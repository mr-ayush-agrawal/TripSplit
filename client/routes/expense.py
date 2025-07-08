import os
from fasthtml.common import fast_app
from fastapi import Request

from client.controller.expense import (
    show_expense, get_edit_expense
)

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
expense_router, rt= fast_app(secret_key=key)


@rt('/{expense_id}')
async def get_one_expense(request: Request, group_id: str, expense_id: str):
    return await show_expense(request, group_id, expense_id)
    
@rt('/{expense_id}/edit')
async def edit_espense(request : Request, group_id : str, expense_id : str):
    # return f"Edit expense feature comming soon for group {group_id} - {expense_id}"
    # if request.method == 'POST':
    #     return await handle_edit_expense(request, group_id, expense_id)
    # elif request.method == 'GET':
        return await get_edit_expense(request, group_id, expense_id)

    
@rt('/{expense_id}/delete')
async def edit_espense(request : Request, group_id : str, expense_id : str):
    return f"Delete expense feature comming soon for group {group_id} - {expense_id}"