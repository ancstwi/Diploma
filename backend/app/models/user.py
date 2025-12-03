from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(100))
    last_name = Column(String(100))
    role = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    scenarios = relationship("BusinessScenario", back_populates="user")