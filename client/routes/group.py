import os, httpx
from fasthtml.common import fast_app, Form
from fastapi.responses import RedirectResponse
from fastapi import Request

from client.pages.group import groups_list_page, create_group_page

from client.static.group.group_style import groups_styles

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
async def create_group_get(request: Request):
    """Create group page - GET"""
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

        return create_group_page(username=username), groups_styles()

    except Exception as e:
        print(f"Error in create group get: {e}")
        return RedirectResponse(url="/user/login", status_code=303)
    
@rt('/create')
async def create_group_post(request: Request, group_name: str, group_description: str = None, base_currency: str = "INR"):
    """Create group page - POST"""
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        # Validate inputs
        if not group_name or len(group_name.strip()) == 0:
            return create_group_page(error_message="Group name is required"), groups_styles()
        
        if len(group_name.strip()) > 50:
            return create_group_page(error_message="Group name must be less than 50 characters"), groups_styles()

        # Prepare data
        group_data = {
            "group_name": group_name.strip(),
            "group_description": group_description.strip() if group_description else None,
            "base_currency": base_currency
        }

        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            # Get username for error display
            user_response = await client.get(f"{backend}/user/", cookies=cookies)
            username = "User"
            if user_response.status_code == 200:
                user_data = user_response.json()
                username = user_data.get("data", {}).get("user_name", "User")
            
            # Create group
            response = await client.post(f"{backend}/group/create-group", json=group_data, cookies=cookies)

        if response.status_code == 200:
            response_data = response.json()
            group_id = response_data.get("group_id")
            # TODO: Redirect to add members page when implemented
            # For now, redirect to groups list
            return RedirectResponse(url="/group/", status_code=303)
        else:
            error_message = response.json().get("detail", "Failed to create group")
            return create_group_page(username=username, error_message=error_message), groups_styles()

    except Exception as e:
        print(f"Error in create group post: {e}")
        return create_group_page(error_message=str(e)), groups_styles()


@rt('/{group_id}')
async def group_details(request: Request, group_id: str):
    """Group details page - TODO: Implement"""
    return f"Group details page for {group_id} - Coming soon!"

@rt('/{group_id}/expense')
async def add_expense(request: Request, group_id: str):
    """Add expense page - TODO: Implement"""
    return f"Add expense page for group {group_id} - Coming soon!"