from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[schemas.Reminder])
def read_reminder(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_reminders = crud.get_reminder(db, user_id=user_id)
    if db_reminders is None:
        raise HTTPException(status_code=404, detail="No Reminders found for this user")
    return db_reminders

@router.get("/", response_model=list[schemas.Reminder])
def read_reminders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reminders = crud.get_reminders(db, skip=skip, limit=limit)
    return reminders

@router.put("/", response_model=schemas.Reminder)
def create_reminder(reminder: schemas.ReminderCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_reminder(db=db, reminder=reminder, user_id=user_id)

@router.patch("/{reminder_id}", response_model=schemas.Reminder)
def update_reminder(reminder_id: int, reminder: schemas.ReminderUpdate, db: Session = Depends(get_db)):
    db_reminder = crud.get_reminder(db, reminder_id=reminder_id)
    if db_reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return crud.update_reminder(db=db, reminder_id=reminder_id, reminder=reminder)

@router.delete("/{reminder_id}", response_model=schemas.Reminder)
def delete_reminder(reminder_id: int, db: Session = Depends(get_db)):
    db_reminder = crud.get_reminder(db, reminder_id=reminder_id)
    if db_reminder is None:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return crud.delete_reminder(db=db, reminder_id=reminder_id)
