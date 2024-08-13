from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime


class ProcedureBase(BaseModel):
    name: str
    notes: str


class ProcedureCreate(ProcedureBase):
    pass


class ProcedureUpdate(ProcedureBase):
    pass


class Procedure(ProcedureBase):
    id: int
    user_id: Optional[int] = None

    class Config:
        from_attributes = True

