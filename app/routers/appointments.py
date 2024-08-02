from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[schemas.Appointment]|schemas.Appointment)
def read_users_appointments(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_appointments = crud.get_users_appointments(db, user_id=user_id)
    return db_appointments

# @router.get("/{appointment_id}", response_model=schemas.Appointment)
# def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
#     db_appointment = crud.get_appointment(db, appointment_id=appointment_id)
#     if db_appointment is None:
#         raise HTTPException(status_code=404, detail="Appointment not found")
#     return db_appointment

@router.get("/", response_model=list[schemas.Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = crud.get_appointments(db, skip=skip, limit=limit)
    return appointments

@router.put("/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_appointment(db=db, appointment=appointment, user_id=user_id)

@router.patch("/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, appointment: schemas.AppointmentUpdate, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return crud.update_appointment(db=db, appointment_id=appointment_id, appointment=appointment)

@router.delete("/{appointment_id}", response_model=schemas.Appointment)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud.get_appointment(db, appointment_id=appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return crud.delete_appointment(db=db, appointment_id=appointment_id)
