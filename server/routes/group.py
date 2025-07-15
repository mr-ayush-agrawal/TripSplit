from fastapi import APIRouter, Depends
from shared.models.group import NewGroup, AddMembersRequest
from shared.models.settlement import NewSettlement
from server.routes.expense import expense_router

from server.middleware.auth import is_logged_in
from server.controller.group import *
from server.controller.settlement import make_settlement
group_router = APIRouter(tags=["Groups"])
group_router.include_router(expense_router, prefix="/{group_id}/expense")


@group_router.get('/') 
async def get_all_user_groups(current_user=Depends(is_logged_in)):
    return get_all_groups(current_user)

@group_router.get('/{group_id}')
async def get_group_info(group_id : str, current_user = Depends(is_logged_in)):
    return group_by_id(group_id, current_user)

@group_router.post('/create-group')
async def create_new_group(group: NewGroup, creator = Depends(is_logged_in)):
    return create_group(group, creator)
    
@group_router.post('/{group_id}/add-member')
async def add_members_to_group(group_id: str, member_list: AddMembersRequest, current_user=Depends(is_logged_in)):
    return add_member(group_id, member_list, current_user)

@group_router.delete("/{group_id}/remove-member/{username}")
async def remove_member_from_group(group_id: str, username: str, current_user=Depends(is_logged_in)):
    return remove_member(group_id, username, current_user)

@group_router.get('/{group_id}/simplified')
async def simplify_group_debts(group_id: str, current_user = Depends(is_logged_in)):
    return simplify(group_id, current_user)

@group_router.post('/{group_id}/settlement')
async def settlement(group_id: str, info : NewSettlement, current_user = Depends(is_logged_in)):
    return make_settlement(group_id, info, current_user) 