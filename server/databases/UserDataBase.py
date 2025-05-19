import sys
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from server.utils.exception import CustomError

load_dotenv()

def connect_user_db(MONGO_DB_URL, DATABASE_NAME, USER_DATA_COLLECTION):
    try:

        client = MongoClient(MONGO_DB_URL, server_api=ServerApi('1'))

        user_collection = client[DATABASE_NAME][USER_DATA_COLLECTION]
        user_collection.create_index("user_id", unique=True)
        user_collection.create_index("email", unique=True)

        print(type(client[DATABASE_NAME][USER_DATA_COLLECTION]))
        print(user_collection.count_documents({}))

        return client

    except Exception as e:
        print('Failed to connect to the database')
        raise CustomError(e, sys)
