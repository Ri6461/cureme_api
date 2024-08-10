from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class AllergyBase(BaseModel):
    name: str
    reaction: str


class AllergyCreate(AllergyBase):
    pass


class Allergy(AllergyBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class AllergyUpdate(AllergyBase):
    pass
