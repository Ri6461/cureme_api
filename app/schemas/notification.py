from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class NotificationBase(BaseModel):
    message: str
    sent_at: datetime


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int
    user_id: int

    class Config:
        from_attributes: Literal[True]


class NotificationUpdate(NotificationBase):
    pass
