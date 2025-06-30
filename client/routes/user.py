import os, httpx
from fasthtml.common import fast_app, Form
from fastapi.responses import RedirectResponse
from client.pages.auth import login_page, signup_page
from shared.models.user import LoginRequest, NewUser
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
user_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')

@rt("/login")
def get():
    return login_page()

@rt('/login')
async def login_post(email : str = None,user_name : str = None, password: str = Form(...)):
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
            response = await client.post(f"{backend}/user/login", json=data)

        if response.status_code == 200:
            return RedirectResponse(url = "/user/", status_code=303)
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



@rt('/')
def get():
    return {
        'page' : 'Home page after login'
    }

@rt("/profile")
def get():
    return {
        'data' : "profile page"
    }

__all__ = ['user_router']