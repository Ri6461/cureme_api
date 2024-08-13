from sqlalchemy.orm import Session
from .. import models, schemas


def get_medical_condition(db: Session, medical_condition_id: int):
    return db.query(models.MedicalCondition).filter(models.MedicalCondition.id == medical_condition_id).first()


def get_user_medical_condition(db: Session, user_id: int):
    return db.query(models.MedicalCondition).filter(models.MedicalCondition.user_id == user_id).all()


def get_medical_conditions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.MedicalCondition).offset(skip).limit(limit).all()


def create_medical_condition(db: Session, medical_condition: schemas.MedicalConditionCreate, user_id: int):
    db_medical_condition = models.MedicalCondition(**medical_condition.dict(), user_id=user_id)
    db.add(db_medical_condition)
    db.commit()
    db.refresh(db_medical_condition)
    return db_medical_condition


def update_medical_condition(db: Session, medical_condition_id: int, medical_condition: schemas.MedicalConditionUpdate):
    db_medical_condition = db.query(models.MedicalCondition).filter(models.MedicalCondition.id == medical_condition_id).first()
    if db_medical_condition:
        for key, value in medical_condition.dict(exclude_unset=True).items():
            setattr(db_medical_condition, key, value)
        db.commit()
        db.refresh(db_medical_condition)
    return db_medical_condition


def delete_medical_condition(db: Session, medical_condition_id: int):
    db_medical_condition = db.query(models.MedicalCondition).filter(models.MedicalCondition.id == medical_condition_id).first()
    if db_medical_condition:
        db.delete(db_medical_condition)
        db.commit()
    return db_medical_condition

