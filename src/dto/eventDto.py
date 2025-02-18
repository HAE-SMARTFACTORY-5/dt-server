from pydantic import BaseModel
from typing import Optional
from src.dto import logDto

class SaveRequest(BaseModel):
	workerId: Optional[int] = None
	cellId: Optional[int] = None
	productId: Optional[int] = None
	robotArmId: Optional[int] = None
	amrId: Optional[int] = None

class EventLogsResponse(BaseModel):
	key: int
	Value: str
	Attributes: list

class EventLogsData(BaseModel):
	workerLog: logDto.WorkerLogResponse
	cellLog: logDto.CellLogResponse
	robotArmLog: logDto.RobotArmLogResponse
	amrLog: logDto.AmrLogResponse