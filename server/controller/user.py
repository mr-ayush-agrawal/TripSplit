from server.classes.user import User
from server.models.user import UserSchema
import sys
from server.utils.exception import CustomError
from server.utils.logger import logging
from pymongo.errors import DuplicateKeyError

async def new_user(user_obj : User, collection):
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


async def update_user_info(user_id: int, collection, new_info: dict):
    '''
    Update user information in the database.
    Args:
        user_id (int): ID of the user to update.
        collection: MongoDB collection to perform the update operation.
        new_info (dict): Dictionary containing the new information to update.
    '''
    logging.info(f"Updating user with id: {user_id}")
    try:
        existing_data = collection.find_one({"user_id": user_id})
        if not existing_data:
            logging.error(f"User with id {user_id} not found.")
            raise CustomError("User not found", sys)
        
        user_data = {
            "user_id": new_info.get("user_id", existing_data["user_id"]),
            "name": new_info.get("name", existing_data["name"]),
            "email": new_info.get("email", existing_data["email"]),
            "base_currency": new_info.get("base_currency", existing_data["base_currency"])
        }


        result = collection.update_one({"user_id": user_id}, {"$set": user_data})
        logging.info(f"User updated with id: {user_id}")

        return result.modified_count

    except Exception as e:
        logging.error(f"Error updating user: {e}")
        raise CustomError(e, sys)