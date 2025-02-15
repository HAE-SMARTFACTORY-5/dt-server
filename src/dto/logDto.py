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
     
class AmrLogRequest(BaseModel):
	amrId: int
	locationX: float
	locationY: float
	locationZ: float
	hight: float
	direction: float
	speed: float
      
class WorkerLogResponse(BaseModel):
    workerId: Optional[int] = None
    cellId: Optional[int] = None
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

    @classmethod
    def of(cls, row):
        return cls(
                workerId=row['worker_id'],
                cellId=row['worker_cell_id'],
                workStatus=row['work_status'],
                locationX=row['worker_location_x'],
                locationY=row['worker_location_y'],
                locationZ=row['worker_location_z'],
                direction=row['worker_direction']
        )

class CellLogResponse(BaseModel):
    cellId: Optional[int] = None
    productId: Optional[int] = None
    processStatus: Optional[str] = None
    completionRate: Optional[float] = None

    @classmethod
    def of(cls, row):
        return cls(
                cellId=row['cell_id'],
                productId=row['product_id'],
                processStatus=row['process_status'],
                completionRate=row['completion_rate']
        )

class RobotArmLogResponse(BaseModel):
    robotArmId: Optional[int] = None
    locationX: Optional[float] = None
    locationY: Optional[float] = None
    locationZ: Optional[float] = None
    direction: Optional[float] = None
    angle1: Optional[float] = None
    angle2: Optional[float] = None
    angle3: Optional[float] = None

    @classmethod
    def of(cls, row):
        return cls(
                robotArmId=row['robot_arm_id'],
                locationX=row['robot_location_x'],
                locationY=row['robot_location_y'],
                locationZ=row['robot_location_z'],
                direction=row['robot_direction'],
                angle1=row['angle_1'],
                angle2=row['angle_2'],
                angle3=row['angle_3']
        )
     
class AmrLogResponse(BaseModel):
    amrId: Optional[int] = None
    locationX: Optional[float] = None
    locationY: Optional[float] = None
    locationZ: Optional[float] = None
    hight: Optional[float] = None
    direction: Optional[float] = None
    speed: Optional[float] = None
    
    @classmethod
    def of(cls, row):
        return cls(
                amrId=row['amr_id'],
                locationX=row['amr_location_x'],
                locationY=row['amr_location_y'],
                locationZ=row['amr_location_z'],
                hight=row['hight'],
                direction=row['amr_direction'],
                speed=row['speed']
        )
    
    
      