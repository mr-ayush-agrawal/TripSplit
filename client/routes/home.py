import os
from client.pages.home import home_page
from fasthtml.common import fast_app
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
home_router, rt = fast_app(secret_key=key)

@rt('/')
def get():
    return home_page()  

__all__ = ['home_router']
