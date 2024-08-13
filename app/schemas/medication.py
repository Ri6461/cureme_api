from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: Optional[date] = None


class MedicationCreate(MedicationBase):
    pass


class Medication(MedicationBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class MedicationUpdate(MedicationBase):
    pass
