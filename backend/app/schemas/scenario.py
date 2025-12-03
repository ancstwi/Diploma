from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ScenarioBase(BaseModel):
    title: str
    description: Optional[str] = None
    industry: Optional[str] = None
    status: Optional[str] = "draft"

class ScenarioCreate(ScenarioBase):
    user_id: str

class ScenarioUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class ScenarioResponse(ScenarioBase):
    id: str
    user_id: str
    created_at: datetime
    
    class Config:
        from_attributes = True