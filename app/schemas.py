from pydantic import BaseModel, EmailStr
from typing import Literal, Optional
from datetime import date, datetime

# User schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str
    dob: date
    phone_number: str
    address: str

class UserCreate(UserBase):
    hashed_password: str
    created_at: datetime
    updated_at: datetime

class UserUpdate(UserBase):
    hashed_password: Optional[str] = None
    updated_at: Optional[datetime] = None
    

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes: Literal[True]

# Medication schemas
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

# Appointment schemas
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

# Reminder schemas
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

# Notification schemas
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

# Contact schemas
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

# Allergy schemas
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

# Medical Condition schemas
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

# Lab schemas
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

# Procedure schemas
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
