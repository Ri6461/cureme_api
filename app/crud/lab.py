from sqlalchemy.orm import Session
from .. import models, schemas


def get_lab(db: Session, lab_id: int):
    return db.query(models.Lab).filter(models.Lab.id == lab_id).first()


def get_user_lab(db: Session, user_id: int):
    return db.query(models.Lab).filter(models.Lab.user_id == user_id).all()


def get_labs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Lab).offset(skip).limit(limit).all()


def create_lab(db: Session, lab: schemas.LabCreate, user_id: int):
    db_lab = models.Lab(**lab.dict(), user_id=user_id)
    db.add(db_lab)
    db.commit()
    db.refresh(db_lab)
    return db_lab


def update_lab(db: Session, lab_id: int, lab: schemas.LabUpdate):
    db_lab = db.query(models.Lab).filter(models.Lab.id == lab_id).first()
    if db_lab:
        for key, value in lab.dict(exclude_unset=True).items():
            setattr(db_lab, key, value)
        db.commit()
        db.refresh(db_lab)
    return db_lab


def delete_lab(db: Session, lab_id: int):
    db_lab = db.query(models.Lab).filter(models.Lab.id == lab_id).first()
    if db_lab:
        db.delete(db_lab)
        db.commit()
    return db_lab
