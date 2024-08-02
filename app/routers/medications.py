from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{medication_id}", response_model=schemas.Medication)
def read_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = crud.get_medication(db, medication_id=medication_id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return db_medication

@router.get("/user/{user_id}", response_model=List[schemas.Medication])
def read_user_medication(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_medications = crud.get_user_medication(db, user_id=user_id)
    if db_medications is None:
        raise HTTPException(status_code=404, detail="Medications not found")
    return db_medications


@router.get("/", response_model=list[schemas.Medication])
def read_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = crud.get_medications(db, skip=skip, limit=limit)
    return medications

@router.put("/", response_model=schemas.Medication)
def create_medication(medication: schemas.MedicationCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_medication(db=db, medication=medication, user_id=user_id)

@router.patch("/{medication_id}", response_model=schemas.Medication)
def update_medication(medication_id: int, medication: schemas.MedicationUpdate, db: Session = Depends(get_db)):
    db_medication = crud.get_medication(db, medication_id=medication_id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return crud.update_medication(db=db, medication_id=medication_id, medication=medication)

@router.delete("/{medication_id}", response_model=schemas.Medication)
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = crud.get_medication(db, medication_id=medication_id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return crud.delete_medication(db=db, medication_id=medication_id)
