from pydantic import BaseModel
from typing import Optional
     
class AmrUpdateRequest(BaseModel):
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

#-------------- Response
     
class AmrResponse(BaseModel):
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
    def withrequest(cls, request: AmrUpdateRequest):
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
    