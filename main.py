from server.databases.config import connect_db
from server.routes.user import user_router
from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException

load_dotenv()
app = FastAPI()
database = connect_db()
user_collection = database[os.getenv('USER_DATA_COLLECTION')]

app.include_router(user_router, prefix='/user')

@app.get('/')
def home():
    return{
        'status_code' : 200,
        'message' : 'Welcome to Home page'
    }

