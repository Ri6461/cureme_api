from sqlalchemy import Column, ForeignKey, Integer, String, Time, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


class Dose(Base):
    __tablename__ = "doses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    medication_id = Column(Integer, ForeignKey("medications.id"))
    time = Column(Time)
    amount = Column(String(50))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    medication = relationship("Medication", back_populates="doses")
