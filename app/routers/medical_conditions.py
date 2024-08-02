from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{medical_condition_id}", response_model=schemas.MedicalCondition)
def read_medical_condition(medical_condition_id: int, db: Session = Depends(get_db)):
    db_medical_condition = crud.get_medical_condition(db, medical_condition_id=medical_condition_id)
    if db_medical_condition is None:
        raise HTTPException(status_code=404, detail="Medical Condition not found")
    return db_medical_condition

@router.get("/user/{medical_condition_id}", response_model=List[schemas.MedicalCondition])
def read_user_medical_condition(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_medical_condition = crud.get_medical_condition(db, user_id=user_id)
    if db_medical_condition is None:
        raise HTTPException(status_code=404, detail="Medical Condition not found")
    return db_medical_condition


@router.get("/", response_model=list[schemas.MedicalCondition])
def read_medical_conditions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medical_conditions = crud.get_medical_conditions(db, skip=skip, limit=limit)
    return medical_conditions

@router.put("/", response_model=schemas.MedicalCondition)
def create_medical_condition(medical_condition: schemas.MedicalConditionCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_medical_condition(db=db, medical_condition=medical_condition, user_id=user_id)

@router.patch("/{medical_condition_id}", response_model=schemas.MedicalCondition)
def update_medical_condition(medical_condition_id: int, medical_condition: schemas.MedicalConditionUpdate, db: Session = Depends(get_db)):
    db_medical_condition = crud.get_medical_condition(db, medical_condition_id=medical_condition_id)
    if db_medical_condition is None:
        raise HTTPException(status_code=404, detail="Medical Condition not found")
    return crud.update_medical_condition(db=db, medical_condition_id=medical_condition_id, medical_condition=medical_condition)

@router.delete("/{medical_condition_id}", response_model=schemas.MedicalCondition)
def delete_medical_condition(medical_condition_id: int, db: Session = Depends(get_db)):
    db_medical_condition = crud.get_medical_condition(db, medical_condition_id=medical_condition_id)
    if db_medical_condition is None:
        raise HTTPException(status_code=404, detail="Medical Condition not found")
    return crud.delete_medical_condition(db=db, medical_condition_id=medical_condition_id)
