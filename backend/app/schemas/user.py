from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "analyst"

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = None

class UserResponse(UserBase):
    id: str
    created_at: datetime
    
    class Config:
        from_attributes = True