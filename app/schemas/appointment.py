from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class AppointmentBase(BaseModel):
    title: str
    notes: str
    appointment_date: datetime


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class AppointmentUpdate(AppointmentBase):
    pass
