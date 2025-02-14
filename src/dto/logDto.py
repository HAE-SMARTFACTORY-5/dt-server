from pydantic import BaseModel
from typing import Optional

class WokerLogRequest(BaseModel):
    workerId: int
    cellId: int
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

class CellLogRequest(BaseModel):
    cellId: int
    productId: Optional[int] = None
    processStatus: str
    completionRate: Optional[float] = None

class RobotArmLogRequest(BaseModel):
	robotArmId: int
	locationX: float
	locationY: float
	locationZ: float
	direction: float
	angle1: float
	angle2: float
	angle3: float