from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Time, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


class VaccineDose(Base):
    __tablename__ = "vaccine_doses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vaccine_id = Column(Integer, ForeignKey("vaccines.id"))
    time = Column(Time)
    amount = Column(String(50))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    vaccine = relationship("Vaccine", back_populates="vaccine_doses")


class Vaccine(Base):
    __tablename__ = "vaccines"

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

    vaccine_doses = relationship("VaccineDose")
    user = relationship("User", back_populates="vaccines")
