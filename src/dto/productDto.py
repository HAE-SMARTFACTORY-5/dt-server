from pydantic import BaseModel
from typing import Optional
     
class ProductSaveRequest(BaseModel):
	customerId: int
	model: str
	color: str

class ProductUpdateRequest(BaseModel):
	amrId: int
	productStatus: str
	processRate: float