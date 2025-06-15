from pydantic import BaseModel, EmailStr, Field, SecretStr
from typing import Optional, List
from datetime import datetime

class NewUser(BaseModel):
    name : str
    email : EmailStr
    user_name : str 
    currency : Optional[str] = 'INR'
    password : SecretStr

class UserResponse(BaseModel):
    name : str
    email : EmailStr
    user_name : str
    currency : str
    hashed_password : str
    groups : List[str] = []
    created_at : datetime = Field(default_factory=datetime.utcnow)

class LoginRequest(BaseModel):
    email: EmailStr
    password: SecretStr
