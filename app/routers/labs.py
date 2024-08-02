from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{lab_id}", response_model=schemas.Lab)
def read_lab(lab_id: int, db: Session = Depends(get_db)):
    db_lab = crud.get_lab(db, lab_id=lab_id)
    if db_lab is None:
        raise HTTPException(status_code=404, detail="Lab not found")
    return db_lab

@router.get("/user/{user_id}", response_model=List[schemas.Lab])
def read_user_lab(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_lab = crud.get_user_lab(db, user_id=user_id)
    if db_lab is None:
        raise HTTPException(status_code=404, detail="Lab not found")
    return db_lab


@router.get("/", response_model=list[schemas.Lab])
def read_labs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    labs = crud.get_labs(db, skip=skip, limit=limit)
    return labs

@router.put("/", response_model=schemas.Lab)
def create_lab(lab: schemas.LabCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_lab(db=db, lab=lab, user_id=user_id)

@router.post("/{lab_id}", response_model=schemas.Lab)
def update_lab(lab_id: int, lab: schemas.LabUpdate, db: Session = Depends(get_db)):
    db_lab = crud.get_lab(db, lab_id=lab_id)
    if db_lab is None:
        raise HTTPException(status_code=404, detail="Lab not found")
    return crud.update_lab(db=db, lab_id=lab_id, lab=lab)

@router.delete("/{lab_id}", response_model=schemas.Lab)
def delete_lab(lab_id: int, db: Session = Depends(get_db)):
    db_lab = crud.get_lab(db, lab_id=lab_id)
    if db_lab is None:
        raise HTTPException(status_code=404, detail="Lab not found")
    return crud.delete_lab(db=db, lab_id=lab_id)
