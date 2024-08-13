from sqlalchemy.orm import Session
from .. import models, schemas


def get_allergy(db: Session, allergy_id: int):
    return db.query(models.Allergy).filter(models.Allergy.id == allergy_id).first()


def get_user_allergy(db: Session, user_id: int):
    return db.query(models.Allergy).filter(models.Allergy.user_id == user_id).all()


def get_allergies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Allergy).offset(skip).limit(limit).all()


def create_allergy(db: Session, allergy: schemas.AllergyCreate, user_id: int):
    db_allergy = models.Allergy(**allergy.dict(), user_id=user_id)
    db.add(db_allergy)
    db.commit()
    db.refresh(db_allergy)
    return db_allergy


def update_allergy(db: Session, allergy_id: int, allergy: schemas.AllergyUpdate):
    db_allergy = db.query(models.Allergy).filter(models.Allergy.id == allergy_id).first()
    if db_allergy:
        for key, value in allergy.dict(exclude_unset=True).items():
            setattr(db_allergy, key, value)
        db.commit()
        db.refresh(db_allergy)
    return db_allergy


def delete_allergy(db: Session, allergy_id: int):
    db_allergy = db.query(models.Allergy).filter(models.Allergy.id == allergy_id).first()
    if db_allergy:
        db.delete(db_allergy)
        db.commit()
    return db_allergy
