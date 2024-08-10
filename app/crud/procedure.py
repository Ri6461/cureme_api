from sqlalchemy.orm import Session
from .. import models, schemas


def get_procedure(db: Session, procedure_id: int):
    return db.query(models.Procedure).filter(models.Procedure.id == procedure_id).first()


def get_user_procedure(db: Session, user_id: int):
    return db.query(models.Procedure).filter(models.Procedure.user_id == user_id).all()


def get_procedures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Procedure).offset(skip).limit(limit).all()


def create_procedure(db: Session, procedure: schemas.ProcedureCreate, user_id: int):
    db_procedure = models.Procedure(**procedure.dict(), user_id=user_id)
    db.add(db_procedure)
    db.commit()
    db.refresh(db_procedure)
    return db_procedure


def delete_procedure(db: Session, procedure_id: int):
    db_procedure = db.query(models.Procedure).filter(models.Procedure.id == procedure_id).first()
    if db_procedure:
        db.delete(db_procedure)
        db.commit()
    return db_procedure


def update_procedure(db: Session, procedure_id: int, procedure: schemas.ProcedureUpdate):
    db_procedure = db.query(models.Procedure).filter(models.Procedure.id == procedure_id).first()
    if db_procedure:
        for key, value in procedure.dict(exclude_unset=True).items():
            setattr(db_procedure, key, value)
        db.commit()
        db.refresh(db_procedure)
    return db_procedure
