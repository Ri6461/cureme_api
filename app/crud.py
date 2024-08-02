from sqlalchemy.orm import Session
from . import models, schemas

# User CRUD operations
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        secret=user.secret,
        username=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        dob=user.dob,
        avatar=user.avatar,
        phone_number=user.phone_number,
        address=user.address,
        created_at=user.created_at,
        updated_at=user.updated_at
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user



# Medication CRUD operations
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

# Appointment CRUD operations
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()

def get_users_appointments(db: Session, user_id: int):
    return db.query(models.Appointment).filter(models.Appointment.user_id == user_id).all()

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

def create_appointment(db: Session, appointment: schemas.AppointmentCreate, user_id: int):
    db_appointment = models.Appointment(**appointment.dict(), user_id=user_id)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db: Session, appointment_id: int, appointment: schemas.AppointmentUpdate):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if db_appointment:
        for key, value in appointment.dict(exclude_unset=True).items():
            setattr(db_appointment, key, value)
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment

# Reminder CRUD operations
def get_reminder(db: Session, user_id: int):
    return db.query(models.Reminder).filter(models.Reminder.user_id == user_id).all()

def get_reminders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reminder).offset(skip).limit(limit).all()

def create_reminder(db: Session, reminder: schemas.ReminderCreate, user_id: int):
    db_reminder = models.Reminder(**reminder.dict(), user_id=user_id)
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

def update_reminder(db: Session, reminder_id: int, reminder: schemas.ReminderUpdate):
    db_reminder = db.query(models.Reminder).filter(models.Reminder.id == reminder_id).first()
    if db_reminder:
        for key, value in reminder.dict(exclude_unset=True).items():
            setattr(db_reminder, key, value)
        db.commit()
        db.refresh(db_reminder)
    return db_reminder

def delete_reminder(db: Session, reminder_id: int):
    db_reminder = db.query(models.Reminder).filter(models.Reminder.id == reminder_id).first()
    if db_reminder:
        db.delete(db_reminder)
        db.commit()
    return db_reminder

# Notification CRUD operations
def get_notification(db: Session, user_id: int):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).all()

def _get_notification(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()

def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).offset(skip).limit(limit).all()

def create_notification(db: Session, notification: schemas.NotificationCreate, user_id: int):
    db_notification = models.Notification(**notification.dict(), user_id=user_id)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def update_notification(db: Session, notification_id: int, notification: schemas.NotificationUpdate):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification:
        for key, value in notification.dict(exclude_unset=True).items():
            setattr(db_notification, key, value)
        db.commit()
        db.refresh(db_notification)
    return db_notification

def delete_notification(db: Session, notification_id: int):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification:
        db.delete(db_notification)
        db.commit()
    return db_notification

# Contact CRUD operations
def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def get_user_contact(db: Session, user_id: int):
    return db.query(models.Contact).filter(models.Contact.user_id == user_id).all()

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: schemas.ContactCreate, user_id: int):
    db_contact = models.Contact(**contact.dict(), user_id=user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: int, contact: schemas.ContactUpdate):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact:
        for key, value in contact.dict(exclude_unset=True).items():
            setattr(db_contact, key, value)
        db.commit()
        db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
    return db_contact

# Allergy CRUD operations
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

# Medical Condition CRUD operations
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


# Lab CRUD operations
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

# Procedure CRUD operations
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
