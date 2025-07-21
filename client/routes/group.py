import os
from fasthtml.common import fast_app
from fastapi import Request

from client.controller.group import (
    create_group_post, create_group_get,
    add_group_members_get, add_group_members_post,
    get_group_home, get_single_group_detail,
    remove_group_members_get, remove_group_members_post,
    get_add_expense, handle_add_expense, get_simplified_debts_page,
    settlement_handler
)
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
group_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')

@rt('/')
async def group_home(request : Request):
    return await get_group_home(request)
    
@rt('/create')
async def create_group(request: Request, group_name: str = None, group_description: str = None, base_currency: str = "INR"):
    if request.method == 'POST':
        return await create_group_post(request, group_name, group_description, base_currency)
    elif request.method == 'GET' :
        return await create_group_get(request)

@rt('/{group_id}/add-members')
async def add_members(request: Request, group_id: str):
    if request.method == 'POST':
        return await add_group_members_post(request, group_id)
    elif request.method == 'GET' :
        return await add_group_members_get(request, group_id)

@rt('/{group_id}')
async def group_details(request: Request, group_id: str):
    """Single group view - displays group details, members, and expenses"""
    return await get_single_group_detail(request, group_id)

@rt('/{group_id}/remove-members')
async def remove_member(request: Request, group_id: str):
    """Remove members page"""
    if request.method == 'POST':
        return await remove_group_members_post(request, group_id)
    elif request.method == 'GET':
        return await remove_group_members_get(request, group_id)

@rt('/{group_id}/add-expense')
async def add_expense(request: Request, group_id: str):
        if request.method == 'POST':
            return await handle_add_expense(request, group_id)
        elif request.method == 'GET':
            return await get_add_expense(request, group_id)




@rt('/{group_id}/simplified-debts')
async def simplify(request: Request, group_id: str):
    """Simplified debts page"""
    return await get_simplified_debts_page(request, group_id)

@rt('/{group_id}/settle', methods=['POST'])
async def settle_payment_page(request: Request, group_id: str):
    return await settlement_handler(request, group_id)