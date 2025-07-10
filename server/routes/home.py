from fastapi import APIRouter, HTTPException, Depends
from server.utils.logger import logging
from server.databases.config import database
from shared.models.feedback import Feedback
from server.middleware.auth import get_user_name

home_router = APIRouter(tags = ['Home'])

feedback_collection = database.get_feedback_collection()

@home_router.get('/')
def home():
    return{
        'status_code' : 200,
        'message' : 'Welcome to Home page'
    }

@home_router.post('/feedback')
def feedback_handler(feedback : Feedback, user_name = Depends(get_user_name)):
    try: 
        logging.info(f'Adding Feedback from {user_name}')
        feedback = feedback.model_dump()
        feedback['user_name'] = user_name

        response = feedback_collection.insert_one(feedback)
        return {
            'status_code': 200,
            'id' : str(response.inserted_id),
            'message' : 'Feedback sent successfully'
        }
        
    except HTTPException as he:
        logging.error(f'Error {str(he)}')
        raise he
    except Exception as e:
        logging.error(f'User signup failed, {e}')
        raise HTTPException(status_code=500, detail=str(e))

