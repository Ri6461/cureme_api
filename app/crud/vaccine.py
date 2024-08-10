from sqlalchemy.orm import Session
from .. import models, schemas


def get_vaccine(db: Session, vaccine_id: int):
    return db.query(models.Vaccine).filter(models.Vaccine.id == vaccine_id).first()


def get_user_vaccine(db: Session, user_id: int):
    return db.query(models.Vaccine).filter(models.Vaccine.user_id == user_id).all()


def get_vaccines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vaccine).offset(skip).limit(limit).all()


def create_vaccine(db: Session, vaccine: schemas.VaccineCreate, user_id: int):
    db_vaccine = models.Vaccine(**vaccine.dict(), user_id=user_id)
    db.add(db_vaccine)
    db.commit()
    db.refresh(db_vaccine)
    return db_vaccine


def update_vaccine(db: Session, vaccine_id: int, vaccine: schemas.VaccineUpdate):
    db_vaccine = db.query(models.Vaccine).filter(models.Vaccine.id == vaccine_id).first()
    if db_vaccine:
        for key, value in vaccine.dict(exclude_unset=True).items():
            setattr(db_vaccine, key, value)
        db.commit()
        db.refresh(db_vaccine)
    return db_vaccine


def delete_vaccine(db: Session, vaccine_id: int):
    db_medication = db.query(models.Vaccine).filter(models.Vaccine.id == vaccine_id).first()
    if db_medication:
        db.delete(db_medication)
        db.commit()
    return db_medication
