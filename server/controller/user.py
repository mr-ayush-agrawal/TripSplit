from server.classes.user import User
from server.models.user import UserSchema
import sys
from server.utils.exception import CustomError
from server.utils.logger import logging
from pymongo.errors import DuplicateKeyError

def new_user(user_obj : User, collection):
    try:
        user_data = {
            "user_id": user_obj.user_id,
            "name": user_obj.name,
            "email": user_obj.email,
            "base_currency": user_obj.currency,
            "hashed_password": "test_hashed_password"
        }

        validated_user = UserSchema(**user_data)
        if not validated_user:
            print('-------User validation failed-------')
            raise CustomError("User data validation failed", sys)

        result = collection.insert_one(validated_user.dict())
        logging.info(f"User inserted with id: {result.inserted_id}")

        return result.inserted_id
    except DuplicateKeyError as e:  
        logging.error(f"User with id {user_obj.user_id} or email {user_obj.email} already exists.")
        raise CustomError("User already exists", sys)
    except Exception as e:
        logging.error(f"Error inserting user: {e}")
        raise CustomError(e, sys)
