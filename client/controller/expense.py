import os, httpx, json
from fastapi.responses import RedirectResponse
from fastapi import Request
from shared.cookie import LOGIN_COOKIE_NAME


from client.pages.expense_detail import expense_detail_page
from client.pages.edit_expense import edit_expense_page
from client.pages.error_pages import group_not_found, group_access_denied

from client.static.group.group_style import groups_styles
from client.static.expense.detail_script import expense_detail_scripts
from client.static.expense.add_style import add_expense_styles
from client.static.expense.style import expense_detail_styles

from dotenv import load_dotenv
load_dotenv()
backend = os.getenv('BACKEND_URL')

async def show_expense(request: Request, group_id: str, expense_id: str):
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

        return (
            expense_detail_page(
                group_id, expense_id,
                username,
                expense_data.get('expense', {}),
                group_data,
                expense_data.get('user_amount', 0.0)
            ), 
            expense_detail_styles(), 
            expense_detail_scripts()
        )

    except Exception as e:
        print(f"Error in expense detail view: {e}")
        return RedirectResponse(url=f"/group/{group_id}", status_code=303)

async def get_edit_expense(request: Request, group_id: str, expense_id: str):
    """Edit expense page with pre-filled form"""
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
            
            # Get group info
            group_response = await client.get(f"{backend}/group/{group_id}", cookies=cookies)
            if group_response.status_code != 200:
                if group_response.status_code == 404:
                    return group_not_found(username), groups_styles()
                elif group_response.status_code == 403:
                    return group_access_denied(username), groups_styles()
                else:
                    return RedirectResponse(url="/group/", status_code=303)
            
            group_data = group_response.json().get("data", {})

            # Get expense info
            expense_response = await client.get(f"{backend}/group/{group_id}/expense/{expense_id}", cookies=cookies)
            if expense_response.status_code != 200:
                return RedirectResponse(url=f"/group/{group_id}", status_code=303)
            
            expense_data = expense_response.json().get('expense', {})
            
            # Check if user is expense owner
            if expense_data.get("expense_owner") != username:
                return RedirectResponse(url=f"/group/{group_id}/expense/{expense_id}", status_code=303)

        return edit_expense_page(
            username=username,
            group_data=group_data,
            expense_data=expense_data,
            group_id=group_id,
            expense_id=expense_id
        ), add_expense_styles()

    except Exception as e:
        print(f"Error in edit expense page: {e}")
        return RedirectResponse(url=f"/group/{group_id}/expense/{expense_id}", status_code=303)

async def handle_edit_expense(request: Request, group_id: str, expense_id: str):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        form_data = await request.form()
        
        # Process form data - same structure as add expense
        expense_data = {
            "title": form_data.get("title"),
            "description": form_data.get("description", ""),
            "amount_original": float(form_data.get("amount", 0)),
            "original_currency": form_data.get("currency"),
            "exchange_rate": float(form_data.get("exchange_rate", 1)),
            "paid_by_original": json.loads(form_data.get("paid_by", "{}")),
            "borrowed_by_original": json.loads(form_data.get("borrowed_by", "{}"))
        }

        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            response = await client.patch(
                f"{backend}/group/{group_id}/expense/{expense_id}/update-expense",
                json=expense_data,
                cookies=cookies
            )
            
        return RedirectResponse(url=f"/group/{group_id}/expense/{expense_id}", status_code=303)

    except Exception as e:
        print(f"Error updating expense: {e}")
        return RedirectResponse(url=f"/group/{group_id}/expense/{expense_id}", status_code=303)

async def handle_delete_expense(request : Request, group_id : str, expense_id : str):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)
        
        cookies = {LOGIN_COOKIE_NAME: auth_cookie}

        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            response = await client.delete(
                f"{backend}/group/{group_id}/expense/{expense_id}/delete",
                cookies=cookies
            )

        if response.status_code == 200:
            # Redirect back to group page after successful deletion
            return RedirectResponse(url=f"/group/{group_id}", status_code=303)
        else:
            # Handle error - redirect to expense detail page with error
            error_detail = response.json().get("detail", "Failed to delete expense")
            return RedirectResponse(
                url=f"/group/{group_id}/expense/{expense_id}?error={error_detail}", 
                status_code=303
            )

    except Exception as e:
        print(f"Error updating expense: {e}")
        return RedirectResponse(url=f"/group/{group_id}/expense/{expense_id}", status_code=303)

