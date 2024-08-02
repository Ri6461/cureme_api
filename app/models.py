from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Text, Time, TIMESTAMP, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(100), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    dob = Column(Date)
    phone_number = Column(String(20))
    address = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    medications = relationship("Medication", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")
    reminders = relationship("Reminder", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
    user_settings = relationship("UserSetting", back_populates="user")
    medical_records = relationship("MedicalRecord", back_populates="user")
    contacts = relationship("Contact", back_populates="user")
    allergies = relationship("Allergy", back_populates="user")
    medical_conditions = relationship("MedicalCondition", back_populates="user")
    labs = relationship("Lab", back_populates="user")
    procedures = relationship("Procedure", back_populates="user")

class Medication(Base):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100), nullable=False)
    dosage = Column(String(50))
    frequency = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    instructions = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    doses = relationship("Dose")
    user = relationship("User", back_populates="medications")

class Dose(Base):
    __tablename__ = "doses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    medication_id = Column(Integer, ForeignKey("medications.id"))
    time = Column(Time)
    amount = Column(String(50))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    medication = relationship("Medication", back_populates="doses")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    doctor_name = Column(String(100))
    title = Column(String(100))
    appointment_date = Column(TIMESTAMP)
    location = Column(String(255))
    notes = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="appointments")

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String(255))
    timestamp = Column(TIMESTAMP)
    type = Column(String(50))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    remind_at = Column(DateTime)

    user = relationship("User", back_populates="reminders")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(String(255))
    # timestamp = Column(TIMESTAMP)
    # created_at = Column(TIMESTAMP)
    # updated_at = Column(TIMESTAMP)
    sent_at = Column(DateTime)

    user = relationship("User", back_populates="notifications")

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    specialization = Column(String(100))
    contact_info = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

class UserSetting(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    setting_name = Column(String(100))
    setting_value = Column(String(100))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="user_settings")

class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    record_type = Column(String(50))
    details = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="medical_records")

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    relation = Column(String(50))
    phone_number = Column(String(20))
    email = Column(String(100))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="contacts")

class Allergy(Base):
    __tablename__ = "allergies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))  # aka. prev (alergen)
    reaction = Column(String(100))
    severity = Column(String(50))
    notes = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="allergies")

class MedicalCondition(Base):
    __tablename__ = "medical_conditions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    condition = Column(String(100))
    diagnosed_date = Column(Date)
    status = Column(String(50))
    notes = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="medical_conditions")

class Lab(Base):
    __tablename__ = "labs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    test_name = Column(String(100))
    test_date = Column(Date)
    results = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="labs")

class Procedure(Base):
    __tablename__ = "procedures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    procedure_name = Column(String(100))
    procedure_date = Column(Date)
    notes = Column(Text)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="procedures")
