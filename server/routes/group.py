from fastapi import APIRouter, Depends
from server.models.group import NewGroup

group_router = APIRouter()

@group_router.get('/') 
def group_test():
    return {
        'message': "Working properly"
    }