from pydantic import BaseModel
from typing import Optional
     
class AmrRequest(BaseModel):
	amrType: str
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


#-------------- Response
     
class AmrResponse(BaseModel):
    amrId: Optional[int] = None
    amrType: Optional[str] = None
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
    def of(cls, amrId, source):
        if isinstance(source, dict):  # `source`가 딕셔너리인 경우
            return cls(
                amrId=amrId,
                amrType=source['amr_type'],
                locationX=source['amr_location_x'],
                locationY=source['amr_location_y'],
                locationZ=source['amr_location_z'],
                height=source['height'],
                direction=source['amr_direction'],
                velocity=source['velocity'],
                state=source['state'],
                destination=source['destination'],
                battery=source['battery'],
                collisionEtected=source['collision_etected'],
            )
        elif isinstance(source, AmrRequest):  # `source`가 특정 클래스인 경우
            return cls(
                amrId=amrId,
                amrType=source.amrType,
                locationX=source.locationX,
                locationY=source.locationY,
                locationZ=source.locationZ,
                height=source.height,
                direction=source.direction,
                velocity=source.velocity,
                state=source.state,
                destination=source.destination,
                battery=source.battery,
                collisionEtected=source.collisionEtected
            )
        else:
            raise TypeError("Invalid argument type. Expected dict or AmrRequest.")
    