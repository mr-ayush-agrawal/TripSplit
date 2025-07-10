import os, httpx
from fasthtml.common import fast_app, Form
from fastapi.responses import RedirectResponse
from fastapi import Request

from client.pages.auth import login_page, signup_page
from client.pages.user import user_dashboard_page
from client.pages.profile import profile_page

from client.static.user.dashboard import dashboard_styles
from client.static.user.profile import profile_styles

from shared.models.user import LoginRequest, NewUser, UpdateUserInfo, UpdatePassword
from shared.cookie import COOKIE_TIMER, LOGIN_COOKIE_NAME, COOKIE_PATH, COOKIE_DOMAIN
from client.routes import REQUEST_HEADER

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
user_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')



@rt("/login")
def get():
    return login_page()

@rt('/login')
async def login_post(request: Request, email: str = None, user_name: str = None, password: str = Form(...)):
    try : 
        data = {"password": password}
        if email : 
            data["email"] = email
        else :
            data["user_name"] = user_name

        # sending request to backend
        data = LoginRequest(**data)
        data = data.model_dump()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{backend}/user/login", json=data, headers=REQUEST_HEADER, cookies=request.cookies)

        if response.status_code == 200:
            cookies_dict = dict(response.cookies)

            redirect_response = RedirectResponse(url="/user/", status_code=303)

            if LOGIN_COOKIE_NAME in cookies_dict:
                redirect_response.set_cookie(
                    key=LOGIN_COOKIE_NAME,
                    value=cookies_dict[LOGIN_COOKIE_NAME],
                    httponly=True,
                    secure=True,
                    samesite="lax",
                    max_age=COOKIE_TIMER,
                    path=COOKIE_PATH
                )
            
            return redirect_response
        else:
            error_message = response.json().get("detail", "Login failed")
            return login_page(error_message) 
    except Exception as e:
        print(e)
        return login_page(str(e))

@rt("/signup")
def get():
    return signup_page()

@rt('/signup')
async def signup_post(name : str, email : str, user_name : str, password : str, re_password: str, currency : str = None):
    try : 
        if password != re_password:
            raise ValueError('Password do not match')
        data = NewUser(name = name, email=email, user_name=user_name, currency=currency, password=password)
        data = data.model_dump()

        async with httpx.AsyncClient() as client:
            response = await client.post(f"{backend}/user/signup", json=data)
        
        if response.status_code == 200: 
            return RedirectResponse(url = "/user/login", status_code=303)
        else:
            error_message = response.json().get("detail", "Login failed")
            return signup_page(error_message) 

    except Exception as e:
        print(e)
        return signup_page(str(e))

@rt('/logout')
async def logout(request : Request):
    try : 
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie : 
            return RedirectResponse(url="/user/login", status_code=303)
        cookies = {LOGIN_COOKIE_NAME: auth_cookie}

        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            response = await client.get(f"{backend}/user/logout",  cookies=cookies)

        if response.status_code == 200:
            redirect = RedirectResponse(url="/user/login", status_code=303)
            redirect.delete_cookie(
                key=LOGIN_COOKIE_NAME,
                domain=COOKIE_DOMAIN,  
                path=COOKIE_PATH
            )
            return redirect
        else:
            error_message = response.json().get("detail", "Login failed")
            return login_page(error_message) 
        
    except Exception as e : 
        print(e)
        return login_page(str(e))
    
@rt('/')
async def user_home(request: Request):
    """User dashboard/home page"""
    try : 
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)
        
        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            response = await client.get(f"{backend}/user/",  cookies=cookies)
        
        if response.status_code == 200:     
            data = response.json()
            username = data.get("data", {}).get("user_name", "John Doe")

            return user_dashboard_page(
                username=username,
            ), dashboard_styles()
        else:
            error_message = response.json().get("detail", "Login failed")
            return RedirectResponse(url="/user/", status_code=303)

    except Exception as e : 
        print(e)
        return login_page(str(e))

@rt("/profile")
async def get(request : Request):
    try : 
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)
        
        cookies = {LOGIN_COOKIE_NAME: auth_cookie}
        async with httpx.AsyncClient(follow_redirects=True, cookies=cookies) as client:
            response = await client.get(f"{backend}/user/profile",  cookies=cookies)

        if response.status_code == 200:
            profile_data = response.json().get("data", {})
            return profile_page(profile_data, total_groups=profile_data.get("stats")), profile_styles()
        
        error_message = response.json().get("detail", "Could not fetch profile")
        return login_page(error_message)

    except Exception as e : 
        print(e)
        return login_page(str(e))

@rt('/profile/update-personal', methods=["POST"])
async def update_personal_info(request: Request, name: str = Form(...)):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        data = {"name": name}
        data = UpdateUserInfo(**data)
        data = data.model_dump()
        async with httpx.AsyncClient() as client:
            cookies = {LOGIN_COOKIE_NAME: auth_cookie}
            res = await client.patch(f"{backend}/user/update-info", json=data, cookies=cookies)

        return RedirectResponse("/user/profile", status_code=303)

    except Exception as e:
        print("Personal Info Update Error:", e)
        return RedirectResponse("/user/profile", status_code=303)

@rt('/profile/update-account', methods=["POST"])
async def update_account_info(request: Request, email: str = Form(...), currency: str = Form(...)):
    try:
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)
        
        data = {"email": email, "currency": currency}
        data = UpdateUserInfo(**data)
        data = data.model_dump()
        async with httpx.AsyncClient() as client:
            cookies = {LOGIN_COOKIE_NAME: auth_cookie}
            res = await client.patch(f"{backend}/user/update-info", json=data, cookies= cookies)

        return RedirectResponse("/user/profile", status_code=303)

    except Exception as e:
        print("Account Info Update Error:", e)
        return RedirectResponse("/user/profile", status_code=303)

@rt('/update-password', methods=["POST"])
async def update_password(request : Request, old_password: str = Form(...), new_password : str = Form(...), confirm_password: str = Form(...)):
    try:
        if new_password != confirm_password:
            raise ValueError("New passwords do not match.")

        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not auth_cookie:
            return RedirectResponse(url="/user/login", status_code=303)

        data = {"old_password": old_password, "new_password": new_password}
        data = UpdatePassword(**data)
        data = data.model_dump()
        async with httpx.AsyncClient() as client:
            cookies = {LOGIN_COOKIE_NAME: auth_cookie}
            res = await client.put(f"{backend}/user/update-password", json=data, cookies=cookies)

        return RedirectResponse("/user/profile", status_code=303)

    except Exception as e:
        print("Password Change Error:", e)
        return RedirectResponse("/user/profile", status_code=303)






__all__ = ['user_router']