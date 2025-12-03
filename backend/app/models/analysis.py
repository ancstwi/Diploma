from sqlalchemy import Column, String, Float, Date, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Analysis(Base):
    __tablename__ = "analysis_data"

    id = Column(String, primary_key=True)
    scenario_id = Column(String, ForeignKey("business_scenarios.id"))
    metric_name = Column(String(100))
    value = Column(Float) 
    date = Column(Date)
    source = Column(String(100))

    scenario = relationship("BusinessScenario", back_populates="analysis_data")

