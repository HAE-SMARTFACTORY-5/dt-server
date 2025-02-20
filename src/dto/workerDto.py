from pydantic import BaseModel
from typing import Optional

class WokerUpdateRequest(BaseModel):
    cellId: int
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

class WokerSaveRequest(BaseModel):
    name: str

#-------------- Response
      
class WorkerResponse(BaseModel):
    workerId: Optional[int] = None
    cellId: Optional[int] = None
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

    @classmethod
    def of(cls, workerId, source: dict):
        if isinstance(source, dict):  # `source`가 딕셔너리인 경우
            return cls(
                workerId=workerId,
                cellId=source['worker_cell_id'],
                workStatus=source['work_status'],
                locationX=source['worker_location_x'],
                locationY=source['worker_location_y'],
                locationZ=source['worker_location_z'],
                direction=source['worker_direction']
            )
        elif isinstance(source, WokerUpdateRequest):  # `source`가 특정 클래스인 경우
            return cls(
                workerId=workerId,
                cellId=source.cellId,
                workStatus=source.workStatus,
                locationX=source.locationX,
                locationY=source.locationY,
                locationZ=source.locationZ,
                direction=source.direction
            )
        else:
            raise TypeError("Invalid argument type. Expected dict or WokerUpdateRequest.")