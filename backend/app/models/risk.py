from sqlalchemy import Column, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Risk(Base):
    __tablename__ = "risks"
    
    id = Column(String, primary_key=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100))
    probability = Column(Float)
    impact = Column(Float)
    severity = Column(Float)
    mitigation_plan = Column(Text)
    scenario_id = Column(String, ForeignKey("business_scenarios.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    scenario = relationship("BusinessScenario", back_populates="risks")