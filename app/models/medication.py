from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


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
