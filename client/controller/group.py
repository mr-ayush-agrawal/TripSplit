import os, httpx
from fastapi.responses import RedirectResponse
from fastapi import Request

from client.pages.group import groups_list_page, create_group_page
from client.pages.add_group_member import add_members_page

from client.static.group.group_style import groups_styles

from shared.cookie import LOGIN_COOKIE_NAME

backend = os.getenv('BACKEND_URL')

async def create_group_post(request: Request, group_name: str = None, group_description: str = None, base_currency: str = "INR"):
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
            response = RedirectResponse(url=f"/group/{group_id}/add-members", status_code=303)
            # response.set_cookie(key="flash_msg", value="Group created successfully!", max_age=5)
            return response
        else:
            error_message = response.json().get("detail", "Failed to create group")
            return create_group_page(username=username, error_message=error_message), groups_styles()

    except Exception as e:
        print(f"Error in create group post: {e}")
        return create_group_page(error_message=str(e)), groups_styles()
    
async def create_group_get(request: Request):
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
    
async def add_group_members_get(request: Request, group_id: str, error_message: str = None, success_message: str = None):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            # Get user info
            user_response = await client.get(f"{backend}/user/", cookies=cookies)
            if user_response.status_code != 200:
                return RedirectResponse(url="/user/login", status_code=303)
            
            user_data = user_response.json()
            username = user_data.get("data", {}).get("user_name", "User")
            
            # Get group info
            group_response = await client.get(f"{backend}/group/{group_id}", cookies=cookies)
            if group_response.status_code != 200:
                return RedirectResponse(url="/group/", status_code=303)
            
            group_data = group_response.json().get("data", {})

        return add_members_page(
            username=username, 
            group_data=group_data, 
            error_message=error_message,
            success_message=success_message
        ), groups_styles()

    except Exception as e:
        print(f"Error in add group members get: {e}")
        return RedirectResponse(url="/group/", status_code=303)

async def add_group_members_post(request: Request, group_id: str):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        # Get form data
        form_data = await request.form()
        usernames_input = form_data.get('usernames', '').strip()
        
        # Validate input
        if not usernames_input:
            return await add_group_members_get(request, group_id, error_message="Please enter at least one username")
        
        # Parse usernames (comma-separated or newline-separated)
        usernames = [username.strip() for username in usernames_input.replace('\n', ',').split(',') if username.strip()]
        
        if not usernames:
            return await add_group_members_get(request, group_id, error_message="Please enter valid usernames")
        
        if len(usernames) > 20:  # Reasonable limit
            return await add_group_members_get(request, group_id, error_message="Cannot add more than 20 members at once")

        # Prepare data for backend
        member_data = {
            "usernames": usernames
        }
        
        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            # Add members to group
            response = await client.post(f"{backend}/group/{group_id}/add-member", json=member_data, cookies=cookies)
            
            if response.status_code == 200:
                response_data = response.json()
                success_message = response_data.get("message", "Members added successfully!")
                members_added = response_data.get("members_added", [])
                
                # Create success message with added members
                if members_added:
                    success_message = f"Successfully added {len(members_added)} members: {', '.join(members_added)}"
                
                return await add_group_members_get(request, group_id, success_message=success_message)
            else:
                error_data = response.json()
                error_message = error_data.get("detail", "Failed to add members")
                return await add_group_members_get(request, group_id, error_message=error_message)

    except Exception as e:
        print(f"Error in add group members post: {e}")
        return await add_group_members_get(request, group_id, error_message="An unexpected error occurred")







