import os
from fasthtml.common import *

from uvicorn import run
from dotenv import load_dotenv
load_dotenv()

from client.routes.home import home_router
from client.routes.user import user_router
from client.routes.group import group_router
from client.routes.expense import expense_router


key = os.getenv('FASTHTML_SESSION_KEY')
app, rt = fast_app(
    secret_key=key,
    static_path='/client/static',
    routes=[
        Mount('/group/{group_id}/expense', expense_router, name = 'expense'),
        Mount('/group/', group_router, name = 'group'),
        Mount('/user/', user_router, name = 'user'),
        Mount('/', home_router, name = 'home'),
    ]
)




if __name__ == '__main__':
    run("frontend:app", host='localhost', port=8080, reload=True)

