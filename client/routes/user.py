import os, httpx
from fasthtml.common import fast_app, Form
from fastapi.responses import RedirectResponse

from client.pages.auth import login_page, signup_page
from client.pages.user import user_dashboard_page
from client.pages.profile import profile_page

from client.static.user.dashboard import dashboard_styles
from client.static.user.profile import profile_styles

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
def user_home():
    """User dashboard/home page"""

    username = "John Doe"  # Get from session
    total_groups = 3
    total_expenses = 15
    balance = 250.50

    return user_dashboard_page(
        username=username,
        total_groups=total_groups,
        total_expenses=total_expenses,
        balance=balance
    ), dashboard_styles()    



@rt("/profile")
def get():
    sample_profile_data =  {
        "name": "John Doe",
        "user_name": "johndoe",
        "email": "john.doe@example.com",
        "currency": "INR"
    }
    profile_data = sample_profile_data
    total_groups = 5  

    return profile_page(profile_data, total_groups=profile_data.get("stats")), profile_styles()


__all__ = ['user_router']