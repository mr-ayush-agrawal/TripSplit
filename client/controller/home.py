import os, httpx
from fastapi import Request
from client.components.home.layout import home_base_layout, feedback_layout
from fastapi.responses import RedirectResponse

from shared.models.feedback import Feedback
from shared.cookie import  LOGIN_COOKIE_NAME

from dotenv import load_dotenv
load_dotenv()

backend = os.getenv('BACKEND_URL')

async def feedback_get():
    content = feedback_layout("Feedback")
    return home_base_layout(title='Feedback', content = content, nav_auth_button=True)

async def feedback_handler(request : Request, title : str, description: str):
    try : 
        auth_cookie = request.cookies.get(LOGIN_COOKIE_NAME)
        if not title or not description:
            raise ValueError("Required both title and description")
        
        data = Feedback(topic=title, description = description)
        data = data.model_dump()

        async with httpx.AsyncClient() as client:
            cookies = {LOGIN_COOKIE_NAME: auth_cookie}
            response = await client.post(f"{backend}/feedback", json=data, cookies= cookies)

        return RedirectResponse('/user/', status_code=303)
        
    except Exception as e:
        print(e)
        return RedirectResponse(url="/user/", status_code=303)