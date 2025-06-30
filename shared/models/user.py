from pydantic import BaseModel, EmailStr, Field, model_validator
from typing import Optional, List
from datetime import datetime

class NewUser(BaseModel):
    name : str
    email : EmailStr
    user_name : str 
    currency : Optional[str] = 'INR'
    password : str

class User(BaseModel):
    name : str
    email : EmailStr
    user_name : str
    currency : str
    hashed_password : str
    groups : List[str] = []
    created_at : datetime = Field(default_factory=datetime.now())

class LoginRequest(BaseModel):
    email: Optional[EmailStr] = None
    user_name: Optional[str] = None
    password: str

    @model_validator(mode = 'after')
    def checkMailandUsername(cls, values):
        if values.email == None and values.user_name==None:
            raise ValueError('Atleast one of email / user name required')
        return values

class UpdateUserInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    currency: Optional[str] = None

class UpdatePassword(BaseModel):
    old_password: str
    new_password: str