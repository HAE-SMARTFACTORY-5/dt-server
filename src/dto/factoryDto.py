from pydantic import BaseModel
     
class FactorySaveRequest(BaseModel):
	name: str