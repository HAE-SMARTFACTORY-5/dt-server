from pydantic import BaseModel
from typing import Optional
     
class ProductRequest(BaseModel):
	customerId: int
	model: str
	color: str