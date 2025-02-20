from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from src.common import constData

class RobotArmUpdateRequest(BaseModel):
	recentStartTime: datetime
	operatingStatus: constData.RobotArmStatus
	locationX: float
	locationY: float
	locationZ: float
	direction: float
	angle1: float
	angle2: float   
	angle3: float
	electric_current: float
	fever: float
    
class RobotArmSaveRequest(BaseModel):
	cellId: int

class RobotArmVibrationRequest(BaseModel):
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
    def of(cls, robotArmId, source):
        if isinstance(source, dict):  # `source`가 딕셔너리인 경우
            return cls(
                robotArmId=robotArmId,
                locationX=source['robot_location_x'],
                locationY=source['robot_location_y'],
                locationZ=source['robot_location_z'],
                direction=source['robot_direction'],
                angle1=source['angle_1'],
                angle2=source['angle_2'],
                angle3=source['angle_3'],
                electric_current=source['electric_current'],
                fever=source['fever']
            )
        elif isinstance(source, RobotArmUpdateRequest):  # `source`가 특정 클래스인 경우
            return cls(
                robotArmId=robotArmId,
                locationX=source.locationX,
                locationY=source.locationY,
                locationZ=source.locationZ,
                direction=source.direction,
                angle1=source.angle1,
                angle2=source.angle2,
                angle3=source.angle3,
                electric_current=source.electric_current,
                fever=source.fever
            )
        else:
            raise TypeError("Invalid argument type. Expected dict or RobotArmUpdateRequest.")
    