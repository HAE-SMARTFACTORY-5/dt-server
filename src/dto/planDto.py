from pydantic import BaseModel
from datetime import date
      
class PlanRequest(BaseModel):
    totalProductionPlan: int
    date: date