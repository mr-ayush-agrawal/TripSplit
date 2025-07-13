import os
from client.pages.home import home_page
from fasthtml.common import fast_app

from client.controller.home import feedback_get, feedback_handler

from fastapi import Request
from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
home_router, rt = fast_app(secret_key=key)

@rt('/')
def get():
    return home_page()  

@rt('/feedback')
async def feedback(request : Request,  title: str = None, description: str = None):
    if request.method == 'GET':
        return await feedback_get(request)
    elif request.method == 'POST':
        return await feedback_handler(request, title, description)

__all__ = ['home_router']
