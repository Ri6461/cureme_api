from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{vaccine_id}", response_model=schemas.Vaccine)
def read_medication(vaccine_id: int, db: Session = Depends(get_db)):
    db_vaccine = crud.get_vaccine(db, vaccine_id=vaccine_id)
    if db_vaccine is None:
        raise HTTPException(status_code=404, detail="Vaccine not found")
    return db_vaccine

@router.get("/user/{user_id}", response_model=List[schemas.Vaccine])
def read_user_medication(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_vaccines = crud.get_user_vaccine(db, user_id=user_id)
    if db_vaccines is None:
        raise HTTPException(status_code=404, detail="Vaccines not found")
    return db_vaccines


@router.get("/", response_model=list[schemas.Vaccine])
def read_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = crud.get_vaccines(db, skip=skip, limit=limit)
    return medications

@router.put("/", response_model=schemas.Vaccine)
def create_medication(vaccine: schemas.VaccineCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_vaccine(db=db, vaccine=vaccine, user_id=user_id)

@router.patch("/{vaccine_id}", response_model=schemas.Vaccine)
def update_medication(vaccine_id: int, vaccine: schemas.VaccineUpdate, db: Session = Depends(get_db)):
    db_vaccine = crud.get_vaccine(db, vaccine_id=vaccine_id)
    if db_vaccine is None:
        raise HTTPException(status_code=404, detail="Vaccine not found")
    return crud.update_vaccine(db=db, vaccine_id=vaccine_id, vaccine=vaccine)

@router.delete("/{vaccine_id}", response_model=schemas.Vaccine)
def delete_medication(vaccine_id: int, db: Session = Depends(get_db)):
    db_vaccine = crud.get_vaccine(db, vaccine_id=vaccine_id)
    if db_vaccine is None:
        raise HTTPException(status_code=404, detail="Vaccine not found")
    return crud.delete_vaccine(db=db, vaccine_id=vaccine_id)
