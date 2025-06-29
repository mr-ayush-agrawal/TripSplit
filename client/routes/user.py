import os
from fasthtml.common import fast_app, APIRouter
from client.pages.auth import login_page, signup_page
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
user_router, rt= fast_app(secret_key=key)

@rt("/login")
def get():
    return login_page()

@rt("/signup")
def get():
    return signup_page()

__all__ = ['user_router']