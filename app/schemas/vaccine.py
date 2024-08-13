from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class VaccineBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: Optional[date] = None


class VaccineCreate(VaccineBase):
    pass


class Vaccine(VaccineBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class VaccineUpdate(VaccineBase):
    pass
