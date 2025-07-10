import os, httpx
from fasthtml.common import fast_app, Form
from fastapi import Request

from client.controller.user import (
    signup_handler, login_handler, logout_handler, home,
    personal_update_handler, account_update_handler,
    password_update_handler, profile_get
)

from client.pages.auth import login_page, signup_page


from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
user_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')


@rt('/login')
async def login(request: Request, email: str = None, user_name: str = None, password: str = Form(...)):
    if request.method == 'POST':
        return await login_handler(request, email, user_name, password)
    elif request.method == 'GET':
        return login_page()

@rt('/signup')
async def signup(request : Request, name : str = None, email : str = None, user_name : str = None, password : str = None, re_password: str = None, currency : str = 'INR'):
    print(request)
    if request.method == 'POST':
        return await signup_handler(name, email, user_name, password, re_password, currency)
    elif request.method == 'GET':
        return signup_page()

@rt('/logout')
async def logout(request : Request):
    return await logout_handler(request)
    
@rt('/')
async def user_home(request: Request):
    return await home(request)

@rt("/profile")
async def get(request : Request):
    return await profile_get(request)

@rt('/profile/update-personal', methods=["POST"])
async def update_personal_info(request: Request, name: str = Form(...)):
    return await personal_update_handler(request, name)

@rt('/profile/update-account', methods=["POST"])
async def update_account_info(request: Request, email: str = Form(...), currency: str = Form(...)):
    return await account_update_handler(request, email, currency)

@rt('/update-password', methods=["POST"])
async def update_password(request : Request, old_password: str = Form(...), new_password : str = Form(...), confirm_password: str = Form(...)):
    return await password_update_handler(request, old_password, new_password, confirm_password)


__all__ = ['user_router']