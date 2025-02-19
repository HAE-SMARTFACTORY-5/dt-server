from pydantic import BaseModel
from typing import Optional

class WokerUpdateRequest(BaseModel):
    workerId: int
    cellId: int
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

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
    def of(cls, row: dict):
        return cls(
                workerId=row['worker_id'],
                cellId=row['worker_cell_id'],
                workStatus=row['work_status'],
                locationX=row['worker_location_x'],
                locationY=row['worker_location_y'],
                locationZ=row['worker_location_z'],
                direction=row['worker_direction']
        )
    @classmethod
    def withrequest(cls, request: WokerUpdateRequest):
        return cls(
                workerId=request.workerId,
                cellId=request.cellId,
                workStatus=request.workStatus,
                locationX=request.locationX,
                locationY=request.locationY,
                locationZ=request.locationZ,
                direction=request.direction
        )