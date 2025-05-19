from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    user_id: int = Field(unique=True)
    name: str
    email: EmailStr = Field(unique=True)
    base_currency: str = Field(default="INR", pattern="^[A-Z]{3}$")
    hashed_password: str 
