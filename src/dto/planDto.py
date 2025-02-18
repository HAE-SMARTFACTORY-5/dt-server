from pydantic import BaseModel
from datetime import date
      
class DailyPlanRequest(BaseModel):
    totalProductionPlan: int
    date: date