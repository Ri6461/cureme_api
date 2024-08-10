from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class ContactBase(BaseModel):
    name: str
    phone_number: str
    email: EmailStr


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class ContactUpdate(ContactBase):
    pass
