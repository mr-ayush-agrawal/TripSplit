from server.databases.config import DatabaseConfig
from server.routes.user import user_router
from server.routes.group import group_router

from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI()
# database = DatabaseConfig()
# user_collection = database.get_user_collection()

app.include_router(user_router, prefix='/user')
app.include_router(group_router, prefix='/group')

@app.get('/')
def home():
    return{
        'status_code' : 200,
        'message' : 'Welcome to Home page'
    }

