from sqlalchemy import Column, ForeignKey, Integer, String, Date, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    avatar = Column(String(1024), unique=False, nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    secret = Column(String(256), nullable=False)
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
    vaccines = relationship("Vaccine", back_populates="user")


class UserSetting(Base):
    __tablename__ = "user_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    setting_name = Column(String(100))
    setting_value = Column(String(100))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    user = relationship("User", back_populates="user_settings")
