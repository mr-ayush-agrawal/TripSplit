from fastapi import APIRouter, Depends, HTTPException
import secrets

from server.models.group import NewGroup
from server.databases.config import DatabaseConfig
from server.middleware.auth import is_logged_in

from server.utils.logger import logging

group_router = APIRouter()
group_collection = DatabaseConfig().get_group_collection()


@group_router.get('/') 
def group_test():
    return {
        'message': "Working properly"
    }

@group_router.post('/create-group')
async def create_group(group: NewGroup, creator = Depends(is_logged_in)):
    try:
        logging.info('Creating new group')
        group_id = await create_unique_group_id()
        group_data = group.model_dump()
        group_data['group_id'] = group_id
        group_data['owner_username'] = creator['user_name']

        group_collection.insert_one(group_data)
        logging.info(f'Group created successfully: {group_data}')
        return {
            'status_code': 201,
            'message': 'Group created successfully',
            'group_id': group_id
        }
    except Exception as e:
        logging.error(f'User signup failed, {e}')
        raise HTTPException(status_code=500, detail=str(e))
    

async def create_unique_group_id():
    i = 0
    while i<100:
        group_id = secrets.token_hex(3)
        exists = group_collection.find_one({"group_id": group_id})
        if not exists:
            return group_id
        i+=1
    logging.error('Failed to generate unique group ID after 100 attempts')
    raise HTTPException(
        status_code=500,
        detail='Failed to generate unique group ID'
    )
    