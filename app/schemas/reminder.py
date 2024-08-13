from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class ReminderBase(BaseModel):
    message: str
    remind_at: datetime


class ReminderCreate(ReminderBase):
    pass


class Reminder(ReminderBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class ReminderUpdate(ReminderBase):
    pass
