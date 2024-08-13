from sqlalchemy.orm import Session
from .. import models, schemas


def get_medication(db: Session, medication_id: int):
    return db.query(models.Medication).filter(models.Medication.id == medication_id).first()


def get_user_medication(db: Session, user_id: int):
    return db.query(models.Medication).filter(models.Medication.user_id == user_id).all()


def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medication).offset(skip).limit(limit).all()


def create_medication(db: Session, medication: schemas.MedicationCreate, user_id: int):
    db_medication = models.Medication(**medication.dict(), user_id=user_id)
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication


def update_medication(db: Session, medication_id: int, medication: schemas.MedicationUpdate):
    db_medication = db.query(models.Medication).filter(models.Medication.id == medication_id).first()
    if db_medication:
        for key, value in medication.dict(exclude_unset=True).items():
            setattr(db_medication, key, value)
        db.commit()
        db.refresh(db_medication)
    return db_medication


def delete_medication(db: Session, medication_id: int):
    db_medication = db.query(models.Medication).filter(models.Medication.id == medication_id).first()
    if db_medication:
        db.delete(db_medication)
        db.commit()
    return db_medication
