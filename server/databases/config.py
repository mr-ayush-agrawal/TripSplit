import sys, os
from pathlib import Path
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
from server.utils.exception import CustomError
from server.utils.logger import logging

load_dotenv()

class DatabaseConfig:
    def __init__(self):
        try:
            self.client = MongoClient(os.getenv('MONGO_DB_URI'), server_api=ServerApi('1'))
            logging.info(f"Connected to MongoDB Client")
            
            self.database = self.client[os.getenv('DATABASE_NAME')]
            self.user_collection = self.database[os.getenv("USER_DATA_COLLECTION")]
            self.user_collection.create_index("email", unique=True)
            self.user_collection.create_index("user_name", unique=True)

            self.group_collection = self.database[os.getenv("GROUP_DATA_COLLECTION")]
            self.group_collection.create_index("group_id", unique=True)

            self.expense_collection = self.database[os.getenv("EXPENSE_DATA_COLLECTION")]
            self.expense_collection.create_index("expense_id", unique=True)

            self.feedback_collection = self.database[os.getenv('FEEDBACK_DATA_COLLECTION')]

            self.settlement_collection = self.database[os.getenv('SETTLEMENT_DATA_COLLECTION')]

        except Exception as e:
            logging.error("Database connection failed")
            print('Failed to connect to the database')
            raise CustomError(e, sys)

    def get_user_collection(self):
        return self.user_collection

    def get_group_collection(self):
        return self.group_collection    
    
    def get_expense_collection(self):
        return self.expense_collection
    
    def get_feedback_collection(self):
        return self.feedback_collection
    
    def get_settlement_collection(self):
        return self.settlement_collection

database = DatabaseConfig()