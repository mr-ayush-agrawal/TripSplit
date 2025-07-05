import os
from fasthtml.common import fast_app
from fastapi import Request

import os, httpx
from fastapi.responses import RedirectResponse
from fastapi import Request
from shared.cookie import LOGIN_COOKIE_NAME

from client.pages.expense_detail import expense_detail_page
from client.static.expense.detail_script import expense_detail_scripts
from client.static.expense.style import expense_detail_styles

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
expense_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')


@rt('/{expense_id}')
async def get_one_expense(request: Request, group_id: str, expense_id: str):
    """
    Updated route handler for expense details
    """
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            # Get current user info
            user_response = await client.get(f"{backend}/user/", cookies=cookies)
            if user_response.status_code != 200:
                return RedirectResponse(url="/user/login", status_code=303)
            
            user_data = user_response.json()
            username = user_data.get("data", {}).get("user_name", "User")
            
            # Get expense details
            expense_response = await client.get(f"{backend}/group/{group_id}/expense/{expense_id}", cookies=cookies)
            if expense_response.status_code != 200:
                return RedirectResponse(url=f"/group/{group_id}", status_code=303)
            
            expense_data = expense_response.json()
            
            # Get group info for members list
            group_response = await client.get(f"{backend}/group/{group_id}", cookies=cookies)
            group_data = group_response.json().get("data", {}) if group_response.status_code == 200 else {}

        return expense_detail_page(
            username,
            expense_data.get('expense', {}),
            group_data,
            expense_data.get('user_amount', 0.0)
        ), expense_detail_styles(), expense_detail_scripts()

    except Exception as e:
        print(f"Error in expense detail view: {e}")
        return RedirectResponse(url=f"/group/{group_id}", status_code=303)
    
@rt('/{expense_id}/edit')
async def edit_espense(request : Request, group_id : str, expense_id : str):
    return f"Edit expense feature comming soon for group {group_id} - {expense_id}"
@rt('/{expense_id}/delete')
async def edit_espense(request : Request, group_id : str, expense_id : str):
    return f"Delete expense feature comming soon for group {group_id} - {expense_id}"