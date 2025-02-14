from pydantic import BaseModel
from typing import Optional

class SaveRequest(BaseModel):
	workerId: Optional[int] = None
	cellId: Optional[int] = None
	productId: Optional[int] = None
	robotArmId: Optional[int] = None
	amrId: Optional[int] = None