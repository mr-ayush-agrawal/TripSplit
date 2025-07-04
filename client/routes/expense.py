import os
from fasthtml.common import fast_app
from fastapi import Request

from dotenv import load_dotenv
load_dotenv()

key = os.getenv('FASTHTML_SESSION_KEY')
expense_router, rt= fast_app(secret_key=key)

backend = os.getenv('BACKEND_URL')

@rt('/{expense_id}')
def get_one_expense(request : Request, group_id:str, expense_id:str):
    return f"Feature comming soom for group {group_id} - expense {expense_id}"