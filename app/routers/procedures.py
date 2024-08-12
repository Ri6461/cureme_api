from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..dependencies import get_current_active_user, verify_role
from ..roles import UserRole

router = APIRouter()

@router.get("/{procedure_id}", response_model=schemas.Procedure)
def read_procedure(procedure_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    db_procedure = crud.get_procedure(db, procedure_id=procedure_id)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return db_procedure

@router.get("/user/{user_id}", response_model=List[schemas.Procedure])
def read_user_procedure(user_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_procedure = crud.get_user_procedure(db, user_id=user_id)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return db_procedure

@router.get("/", response_model=List[schemas.Procedure])
def read_procedures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_active_user)):
    procedures = crud.get_procedures(db, skip=skip, limit=limit)
    return procedures

@router.put("/", response_model=schemas.Procedure)
def create_procedure(procedure: schemas.ProcedureCreate, user_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(verify_role(UserRole.DOCTOR))):
    return crud.create_procedure(db=db, procedure=procedure, user_id=user_id)

@router.patch("/{procedure_id}", response_model=schemas.Procedure)
def update_procedure(procedure_id: int, procedure: schemas.ProcedureUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(verify_role(UserRole.DOCTOR))):
    db_procedure = crud.get_procedure(db, procedure_id=procedure_id)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return crud.update_procedure(db=db, procedure_id=procedure_id, procedure=procedure)

@router.delete("/{procedure_id}", response_model=schemas.Procedure)
def delete_procedure(procedure_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(verify_role(UserRole.DOCTOR))):
    db_procedure = crud.get_procedure(db, procedure_id=procedure_id)
    if db_procedure is None:
        raise HTTPException(status_code=404, detail="Procedure not found")
    return crud.delete_procedure(db=db, procedure_id=procedure_id)