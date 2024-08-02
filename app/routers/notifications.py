from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{user_id}", response_model=List[schemas.Notification])
def read_notification(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_notification = crud.get_notification(db, user_id=user_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="No Notifications found for this user.")
    return db_notification

@router.get("/", response_model=list[schemas.Notification])
def read_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notifications = crud.get_notifications(db, skip=skip, limit=limit)
    return notifications

@router.put("/", response_model=schemas.Notification)
def create_notification(notification: schemas.NotificationCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_notification(db=db, notification=notification, user_id=user_id)

@router.patch("/{notification_id}", response_model=schemas.Notification)
def update_notification(notification_id: int, notification: schemas.NotificationUpdate, db: Session = Depends(get_db)):
    db_notification = crud._get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.update_notification(db=db, notification_id=notification_id, notification=notification)

@router.delete("/{notification_id}", response_model=schemas.Notification)
def delete_notification(notification_id: int, db: Session = Depends(get_db)):
    db_notification = crud._get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.delete_notification(db=db, notification_id=notification_id)
