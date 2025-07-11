from server.routes.user import user_router
from server.routes.group import group_router
from server.routes.home import home_router
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
app.include_router(home_router, prefix='/api')
