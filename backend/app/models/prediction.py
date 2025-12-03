from sqlalchemy import Column, String, JSON, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(String, primary_key=True)
    scenario_id = Column(String, ForeignKey("business_scenarios.id"))
    model_type = Column(String(50)) 
    input_data = Column(JSON)
    output_data = Column(JSON) 
    accuracy = Column(Float) 
    created_at = Column(DateTime, server_default=func.now())

    scenario = relationship("BusinessScenario", back_populates="predictions")
