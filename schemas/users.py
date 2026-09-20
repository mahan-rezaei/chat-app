from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime