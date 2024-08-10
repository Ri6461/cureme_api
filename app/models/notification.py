from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..database import Base


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
