from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from ..database import Base


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

