from fastapi import APIRouter, HTTPException, Depends
from server.models.user import NewUser, UserResponse, LoginRequest
from server.utils.password_hash import hash_password, verify_password
from server.utils.logger import logging
from server.databases.config import connect_db
# from server.controller.user import new_user, update_user_info
import os

user_router = APIRouter()
database = connect_db()
user_collection = database[os.getenv('USER_DATA_COLLECTION')]


@user_router.post("/signup")
async def signup(user: NewUser):
    try:
        logging.info('Starting user signup')

        # Checking for existing useres
        existing_user = user_collection.find_one({"email": user.email})
        if existing_user:
            logging.error(f'User with email {user.email} alredy exist')
            raise HTTPException(status_code=400, detail="Email already registered")
        existing_user = user_collection.find_one({"user_name": user.user_name})

        if existing_user:
            logging.error(f'User with user name {user.user_name} alredy exist')
            raise HTTPException(status_code=400, detail="Email already registered")


        user_obj = user.dict()
        user_obj['password'] = hash_password(user_obj['password'].get_secret_value())

        resp = user_collection.insert_one(user_obj)

        logging.info('User data added succesfully')
        return {
            'status_code' : 200,
            'id' : str(resp.inserted_id)
        }
    except Exception as e:
        logging.error('User signup failed')
        raise HTTPException(status_code=500, detail=str(e))


# @router.patch("/modify_user/{user_id}")
# async def update_user(user_id: int, newinfo: dict):
#     try:
#         await update_user_info(user_id, user_db_client[USER_DATABASE_NAME][USER_COLLECTION], newinfo)
#         return {"user_id": str(user_id)}
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))