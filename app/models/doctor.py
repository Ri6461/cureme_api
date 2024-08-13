from sqlalchemy import Column, Integer, String, TIMESTAMP  # , ForeignKey
# from sqlalchemy.orm import relationship
from ..database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    specialization = Column(String(100))
    contact_info = Column(String(255))
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

