from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WokerUpdateRequest(BaseModel):
    workerId: int
    cellId: int
    workStatus:	Optional[str] = None
    locationX:	Optional[float] = None
    locationY:	Optional[float] = None
    locationZ:	Optional[float] = None
    direction:	Optional[float] = None

class CellLogRequest(BaseModel):
    cellId: int
    recentStartTime: datetime
    productId: Optional[int] = None
    processStatus: str
    completionRate: Optional[float] = None

class RobotArmLogRequest(BaseModel):
	robotArmId: int
	recentStartTime: datetime
	operatingStatus: str
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
	height: float
	direction: float
	velocity: float
	destination: str
	battery: float
	collisionEtected: bool
	state: str


class RobotArmStatusRequest(BaseModel):
    robotArmId: int
    fever: float
    electricCurrent: float
    vibration: float


#-------------- Response
      
class WorkerLogResponse(BaseModel):
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
    
    @classmethod
    def withrequest(cls, request: CellLogRequest):
        return cls(
                cellId=request.cellId,
                productId=request.productId,
                processStatus=request.processStatus,
                completionRate=request.completionRate
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
    
    @classmethod
    def withrequest(cls, request: RobotArmLogRequest):
        return cls(
                robotArmId=request.robotArmId,
                locationX=request.locationX,
                locationY=request.locationY,
                locationZ=request.locationZ,
                direction=request.direction,
                angle1=request.angle1,
                angle2=request.angle2,
                angle3=request.angle3,
        )
     
class AmrLogResponse(BaseModel):
    amrId: Optional[int] = None
    locationX: Optional[float] = None
    locationY: Optional[float] = None
    locationZ: Optional[float] = None
    height: Optional[float] = None
    direction: Optional[float] = None
    velocity: Optional[float] = None
    state: Optional[str] = None
    destination: Optional[str] = None
    battery: Optional[float] = None
    collisionEtected: Optional[bool] = None

    @classmethod
    def of(cls, row):
        return cls(
                amrId=row['amr_id'],
                locationX=row['amr_location_x'],
                locationY=row['amr_location_y'],
                locationZ=row['amr_location_z'],
                height=row['height'],
                direction=row['amr_direction'],
                velocity=row['velocity'],
                state=row['state'],
                destination=row['destination'],
                battery=row['battery'],
                collisionEtected=row['collision_etected'],
        )
    
    @classmethod
    def withrequest(cls, request: AmrLogRequest):
        return cls(
                amrId=request.amrId,
                locationX=request.locationX,
                locationY=request.locationY,
                locationZ=request.locationZ,
                height=request.height,
                direction=request.direction,
                velocity=request.velocity,
                state=request.state,
                destination=request.destination,
                battery=request.battery,
                collisionEtected=request.collisionEtected
        )
    