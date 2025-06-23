import sys, os
from fastapi import HTTPException, Response, Depends

from server.databases.config import database
from server.models.user import NewUser, LoginRequest
from server.middleware.auth import is_logged_in

from server.utils.logger import logging
from server.utils.password_hash import hash_password,verify_password
from server.utils.jwt_auth import create_access_token

from server.utils import COOKIE_TIMER, LOGIN_COOKIE_NAME


user_collection = database.get_user_collection()


# ------------ Routes Functions ---------------------
def signup(user: NewUser):
    try : 
        # Checking for existing useres
        existing_user = user_collection.find_one({"email": user.email})
        if existing_user:
            logging.error(f'User with email {user.email} alredy exist')
            raise HTTPException(status_code=400, detail="Email already registered")
        existing_user = user_collection.find_one({"user_name": user.user_name})

        if existing_user:
            logging.error(f'User with user name {user.user_name} alredy exist')
            raise HTTPException(status_code=400, detail="Email already registered")

        user_obj = user.model_dump()
        user_obj['password'] = hash_password(user_obj['password'])

        resp = user_collection.insert_one(user_obj)
        print(user_obj)

        logging.info('User data added succesfully')
        return {
            'status_code' : 200,
            'id' : str(resp.inserted_id)
        }
    except Exception as e:
        logging.error(f'User signup failed, {e}')
        raise HTTPException(status_code=500, detail=str(e))


def login(login_data : LoginRequest, response : Response):
    try:
        logging.info('Login Attempt')
        if login_data.email : 
            user = user_collection.find_one({"email": login_data.email}) 
        elif login_data.user_name:
            user = user_collection.find_one({"user_name": login_data.user_name})
        else : 
            raise HTTPException(status_code=400, detail="Email or Username required")

        if not user : 
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(login_data.password, user['password']):
            raise HTTPException(status_code=401, detail="Incorrect password")

        token_data = {
            "user_id": str(user["_id"]),
            "email": user["email"],
            "user_name": user["user_name"]
        }
        token = create_access_token(data=token_data)

        response.set_cookie(
            key=LOGIN_COOKIE_NAME,
            value=token,
            httponly=True,
            secure=False,  # Set to True in production with HTTPS
            samesite="lax",  # or 'strict'/'none'
            max_age=COOKIE_TIMER  # in seconds
        )

        logging.info(f'Login succesful for user : {user['user_name']}')
        return {"status_code": 200, "message": "Login successful"}
    except HTTPException as e : 
        logging.error(f"Login failed: {e.status_code} - {e.detail}")
        raise e
    except Exception as e : 
        logging.error(f"Login failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def logout(response: Response, user):
    try : 
        response.delete_cookie(LOGIN_COOKIE_NAME)
        logging.info("User logged out")
        return {"status_code": 200, "message": f"{user['user_name']} logged out successfully"}
    except :
        logging.error('Error Logging out')
        raise HTTPException(status_code=400, detail="Can't log out the user")

def get_profile(user):
    logging.info("Getting the user info")
    return {
        "status_code": 200,
        "user": user
    }




# ------------ Prior -----------------
# from server.utils.exception import CustomError
# from pymongo.errors import DuplicateKeyError

# async def new_user(user_obj : User, collection):
#     try:
#         user_data = {
#             "user_id": user_obj.user_id,
#             "name": user_obj.name,
#             "email": user_obj.email,
#             "base_currency": user_obj.currency,
#             "hashed_password": "test_hashed_password"
#         }

#         validated_user = UserSchema(**user_data)
#         if not validated_user:
#             raise CustomError("User data validation failed", sys)

#         result = collection.insert_one(validated_user.dict())
#         logging.info(f"User inserted with id: {result.inserted_id}")

#         return result.inserted_id
#     except DuplicateKeyError as e:  
#         logging.error(f"User with id {user_obj.user_id} or email {user_obj.email} already exists.")
#         raise CustomError("User already exists", sys)
#     except Exception as e:
#         logging.error(f"Error inserting user: {e}")
#         raise CustomError(e, sys)


# async def update_user_info(user_id: int, collection, new_info: dict):
#     '''
#     Update user information in the database.
#     Args:
#         user_id (int): ID of the user to update.
#         collection: MongoDB collection to perform the update operation.
#         new_info (dict): Dictionary containing the new information to update.
#     '''
#     logging.info(f"Updating user with id: {user_id}")
#     try:
#         existing_data = collection.find_one({"user_id": user_id})
#         if not existing_data:
#             logging.error(f"User with id {user_id} not found.")
#             raise CustomError("User not found", sys)
        
#         user_data = {
#             "user_id": new_info.get("user_id", existing_data["user_id"]),
#             "name": new_info.get("name", existing_data["name"]),
#             "email": new_info.get("email", existing_data["email"]),
#             "base_currency": new_info.get("base_currency", existing_data["base_currency"])
#         }


#         result = collection.update_one({"user_id": user_id}, {"$set": user_data})
#         logging.info(f"User updated with id: {user_id}")

#         return result.modified_count

#     except Exception as e:
#         logging.error(f"Error updating user: {e}")
#         raise CustomError(e, sys)