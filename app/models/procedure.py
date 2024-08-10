from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


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


