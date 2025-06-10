from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    user_id : str
    name : str
    email : EmailStr
    currency : Optional[str] = 'INR'
    password : str
    friends : Optional[List['User']] = None
    created_at : datetime = datetime.now()


User.rebuild_model()