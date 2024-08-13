from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class LabBase(BaseModel):
    name: str
    result: str
    date: datetime


class LabCreate(LabBase):
    pass


class Lab(LabBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class LabUpdate(LabBase):
    pass
