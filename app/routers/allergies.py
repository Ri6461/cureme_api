from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{allergy_id}", response_model=schemas.Allergy)
def read_allergy(allergy_id: int, db: Session = Depends(get_db)):
    db_allergy = crud.get_allergy(db, allergy_id=allergy_id)
    if db_allergy is None:
        raise HTTPException(status_code=404, detail="Allergy not found")
    return db_allergy

@router.get("/user/{user_id}", response_model=schemas.Allergy)
def read_user_allergy(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_allergy = crud.get_user_allergy(db, user_id=user_id)
    if db_allergy is None:
        raise HTTPException(status_code=404, detail="Allergy not found")
    return db_allergy


@router.get("/", response_model=list[schemas.Allergy])
def read_allergies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    allergies = crud.get_allergies(db, skip=skip, limit=limit)
    return allergies

@router.put("/", response_model=schemas.Allergy)
def create_allergy(allergy: schemas.AllergyCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_allergy(db=db, allergy=allergy, user_id=user_id)

@router.patch("/{allergy_id}", response_model=schemas.Allergy)
def update_allergy(allergy_id: int, allergy: schemas.AllergyUpdate, db: Session = Depends(get_db)):
    db_allergy = crud.get_allergy(db, allergy_id=allergy_id)
    if db_allergy is None:
        raise HTTPException(status_code=404, detail="Allergy not found")
    return crud.update_allergy(db=db, allergy_id=allergy_id, allergy=allergy)

@router.delete("/{allergy_id}", response_model=schemas.Allergy)
def delete_allergy(allergy_id: int, db: Session = Depends(get_db)):
    db_allergy = crud.get_allergy(db, allergy_id=allergy_id)
    if db_allergy is None:
        raise HTTPException(status_code=404, detail="Allergy not found")
    return crud.delete_allergy(db=db, allergy_id=allergy_id)
