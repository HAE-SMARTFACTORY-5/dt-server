from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RobotArmUpdateRequest(BaseModel):
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
	electric_current: float
	fever: float

class RobotArmVibrationUpdateRequest(BaseModel):
    robotArmId: int
    vibration: float


#-------------- Response

class RobotArmResponse(BaseModel):
    robotArmId: Optional[int] = None
    locationX: Optional[float] = None
    locationY: Optional[float] = None
    locationZ: Optional[float] = None
    direction: Optional[float] = None
    angle1: Optional[float] = None
    angle2: Optional[float] = None
    angle3: Optional[float] = None
    electric_current: Optional[float] = None
    fever: Optional[float] = None

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
                angle3=row['angle_3'],
                electric_current=row['electric_current'],
                fever=row['fever']
        )
    
    @classmethod
    def withrequest(cls, request: RobotArmUpdateRequest):
        return cls(
                robotArmId=request.robotArmId,
                locationX=request.locationX,
                locationY=request.locationY,
                locationZ=request.locationZ,
                direction=request.direction,
                angle1=request.angle1,
                angle2=request.angle2,
                angle3=request.angle3,
                electric_current=request.electric_current,
                fever=request.fever
        )
    