from fastapi import APIRouter, HTTPException, Depends
from server.controller.user import new_user
from server.classes.user import User
from server.models.user import UserSchema
from server.databases.UserDataBase import connect_user_db
import os

router = APIRouter()

MONGO_DB_URL = os.getenv("MONGO_DB_URI")
USER_DATABASE_NAME = os.getenv("DATABASE_NAME")
USER_COLLECTION = os.getenv("USER_DATA_COLLECTION")
user_db_client = connect_user_db(MONGO_DB_URL, USER_DATABASE_NAME, USER_COLLECTION)

@router.post("/signup")
def signup(user: UserSchema):
    try:
        user_obj = User(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            currency=getattr(user, 'base_currency', getattr(user, 'currency', 'INR'))
        )
        user_id = new_user(user_obj, user_db_client[USER_DATABASE_NAME][USER_COLLECTION])
        return {"user_id": str(user_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
