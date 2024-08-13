from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class MedicalConditionBase(BaseModel):
    name: str
    description: str


class MedicalConditionCreate(MedicalConditionBase):
    pass


class MedicalCondition(MedicalConditionBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class MedicalConditionUpdate(MedicalConditionBase):
    pass
