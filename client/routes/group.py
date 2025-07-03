import os, httpx
from fasthtml.common import fast_app, Form
from fastapi.responses import RedirectResponse
from fastapi import Request

from client.pages.group import groups_list_page, create_group_page

from client.static.group.group_style import groups_styles

from client.controller.group import (
    create_group_post, create_group_get, add_group_members_get, add_group_members_post
)

from shared.cookie import LOGIN_COOKIE_NAME

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
group_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')

@rt('/')
async def group_home(request : Request):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            user_response = await client.get(f"{backend}/user/", cookies=cookies)
            if user_response.status_code != 200:
                return RedirectResponse(url="/user/login", status_code=303)

            user_data = user_response.json()
            username = user_data.get("data", {}).get("user_name", "User")
            groups_response = await client.get(f"{backend}/group/", cookies=cookies)
            if groups_response.status_code == 200:
                groups_data = groups_response.json()
                user_groups = groups_data.get("user_groups", [])
            else:
                user_groups = []

        return groups_list_page(
            username=username,
            user_groups=user_groups
        ), groups_styles()

    except Exception as e:
        print(f"Error fetching groups: {e}")
        return groups_list_page([], str(e))
    
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
    """Group details page - TODO: Implement"""
    # flash_msg = request.cookies.get("flash_msg")
    # response = group_detail_page(group_id=group_id, success_msg=flash_msg), group_styles()

    # if flash_msg:
    #     # Clear the flash message so it's not shown again
    #     final_response = HTMLResponse(content=str(response[0]))
    #     final_response.delete_cookie("flash_msg")
    #     return final_response, response[1]

    # return response
    return f"Group details page for {group_id} - Coming soon!"

@rt('/{group_id}/expense')
async def add_expense(request: Request, group_id: str):
    """Add expense page - TODO: Implement"""
    return f"Add expense page for group {group_id} - Coming soon!"