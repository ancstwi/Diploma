from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class BusinessScenario(Base):
    __tablename__ = "business_scenarios"

    id = Column(String, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    industry = Column(String(100))
    status = Column(String(50), default="draft")
    user_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="scenarios")
    risks = relationship("Risk", back_populates="scenario")
    analysis_data = relationship("Analysis", back_populates="scenario")
    predictions = relationship("Prediction", back_populates="scenario")