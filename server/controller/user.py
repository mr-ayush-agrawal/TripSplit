from fastapi import HTTPException, Response

from server.databases.config import database
from shared.models.user import *

from server.utils.logger import logging
from server.utils.password_hash import hash_password,verify_password
from server.utils.jwt_auth import create_access_token

from server.utils import COOKIE_TIMER, LOGIN_COOKIE_NAME


user_collection = database.get_user_collection()


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
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
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

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e : 
        logging.error(f"Login failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def logout(response: Response, user : User):
    try : 
        response.delete_cookie(LOGIN_COOKIE_NAME)
        logging.info("User logged out")
        return {"status_code": 200, "message": f"{user['user_name']} logged out successfully"}
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error('Error Logging out')
        raise HTTPException(status_code=400, detail=f"Can't log out the user {str(e)}")

def get_profile(user : User):
    logging.info("Getting the user info")
    try:
        exclude_fields = {'password', '_id'}
        profile = {k: v for k, v in user.items() if k not in exclude_fields}
        return {
            "status_code": 200,
            "data": profile
        }

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f"Missing expected user field: {e}")
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")

def update_info(newinfo : UpdateUserInfo, user: User):
    try : 
        user_name = user['user_name']
        update_fields = {}

        # Only update provided fields
        for field in ['name', 'email', 'currency']:
            if newinfo.get(field):
                update_fields[field] = newinfo[field]
        if not update_fields:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        result = user_collection.update_one(
            {"user_name": user_name},
            {"$set": update_fields}
        )
        if result.modified_count == 0:
            raise HTTPException(status_code=400, detail="No changes made")

        logging.info(f"User {user_name} updated info: {update_fields}")
        return {"status_code": 200, "message": "User info updated"}

    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f"Failed to update the user info : {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
def update_password(newinfo: UpdatePassword, current_user: User):
    try :
        user_name = current_user['user_name']
        user = user_collection.find_one({"user_name": user_name})

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(newinfo['old_password'], user['password']):
            raise HTTPException(status_code=401, detail="Incorrect old password")
        
        hashed_new_password = hash_password(newinfo['new_password'])
        user_collection.update_one(
            {"user_name": user_name},
            {"$set": {"password": hashed_new_password}}
        )
        logging.info(f"Password updated for user {user_name}")
        return {"status_code": 200, "message": "Password updated successfully"}
    
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f"Failed to find the user for password update: {e}")
        raise HTTPException(status_code=500, detail=str(e))