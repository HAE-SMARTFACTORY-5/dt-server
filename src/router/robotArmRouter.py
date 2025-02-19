from fastapi import APIRouter
from src.service import robotArmService
from src.dto import robotArmDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="로봇 팔 정보 업데이트")
async def updateRobotArm(request: robotArmDto.RobotArmUpdateRequest) -> str:
    result = robotArmService.updateRobotArm(request)
    jsonResult = socketDto.SocketTypeResponse.of("ROBOT-ARM", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"

@api.post("/vibrations", summary="로봇 팔 진동상태 업데이트")
async def updateRobotArmVibration(request: robotArmDto.RobotArmVibrationUpdateRequest) -> str:
    result = robotArmService.updateRobotArmVibration(request)
    jsonResult = socketDto.SocketTypeResponse.of("ROBOT-ARM-STATUS", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"