from server.routes.user import user_router
from server.routes.group import group_router
import uvicorn

import os
from fastapi import FastAPI
from uvicorn import run
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(user_router, prefix='/user')
app.include_router(group_router, prefix='/group')

@app.get('/')
def home():
    return{
        'status_code' : 200,
        'message' : 'Welcome to Home page'
    }

if __name__ == '__main__':
    # run("main:app", host='localhost', port=8000, reload=True)
    config = uvicorn.Config(
        "main:app",
        host="localhost",
        port=8000,
        reload=True,
        reload_excludes=["logs/*"]
    )
    server = uvicorn.Server(config)
    server.run() 
