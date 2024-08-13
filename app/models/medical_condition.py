from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


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

