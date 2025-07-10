from server.routes.user import user_router
from server.routes.group import group_router
from fastapi.middleware.cors import CORSMiddleware

import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://nishka-gamma.vercel.app", "*"],  # Specify exact origins
    allow_credentials=True,         # This is crucial for cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix='/api/user')
app.include_router(group_router, prefix='/api/group')

@app.get('/api/')
def home():
    return{
        'status_code' : 200,
        'message' : 'Welcome to Home page'
    }

# if __name__ == '__main__':
#     # run("main:app", host='localhost', port=8000, reload=True)
#     config = uvicorn.Config(
#         "main:app",
#         host="localhost",
#         port=8000,
#         reload=True,
#         reload_excludes=["logs/*"]
#     )
#     server = uvicorn.Server(config)
#     server.run() 
