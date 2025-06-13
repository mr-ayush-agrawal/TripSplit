import sys, os
from pathlib import Path
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
from server.utils.exception import CustomError
from server.utils.logger import logging

env_path = Path('server') / '.env'
load_dotenv(dotenv_path=env_path)

MONGO_DB_URL = os.getenv('MONGO_DB_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')

def connect_db():
    try:
        client = MongoClient(MONGO_DB_URL, server_api=ServerApi('1'))
        logging.info(f"Connected to MongoDB Client")

        database = client[DATABASE_NAME]
        logging.info(f"Reterived Database")
        return database

    except Exception as e:
        logging.error("Database connection failed")
        print('Failed to connect to the database')
        raise CustomError(e, sys)
