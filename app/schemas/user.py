from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    dob: date
    phone_number: str
    avatar: Optional[str]
    address: str


class UserLogin(BaseModel):
    email: EmailStr
    secret: str


class UserAuth(BaseModel):
    token: str


class UserCreate(UserBase):
    secret: str
    created_at: datetime
    updated_at: datetime


class UserUpdate(UserBase):
    secret: Optional[str] = None
    updated_at: Optional[datetime] = None
    

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes: Literal[True]
