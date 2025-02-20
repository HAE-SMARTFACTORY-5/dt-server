from fastapi import APIRouter
from src.service import robotArmService, widgetService
from src.dto import robotArmDto
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

api = APIRouter()

@api.post("/{robotArmId}", summary="로봇 팔 정보 업데이트")
async def updateRobotArm(robotArmId: int, request: robotArmDto.RobotArmUpdateRequest) -> str:
    robotArmResponse = robotArmService.update(robotArmId, request)
    robotArmWidgetResponse = widgetService.getRobotArmWidget(robotArmId)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.ROBOT_ARM, robotArmResponse)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.ROBOT_ARM_WIDGET, robotArmWidgetResponse)
    return "OK"

@api.post("", summary="로봇 팔 등록")
async def saveRobotArm(request: robotArmDto.RobotArmSaveRequest) -> str:
    robotArmService.saveRobotArm(request)
    return "OK"

@api.post("/{robotArmId}/vibrations", summary="로봇 팔 진동상태 저장")
async def saveRobotArmVibration(romotArmId: int, request: robotArmDto.RobotArmVibrationRequest) -> str:
    robotArmResponse = robotArmService.saveRobotArmVibration(romotArmId, request)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.ROBOT_ARM_VIBRATION, robotArmResponse)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.ROBOT_ARM_WIDGET, robotArmResponse)
    return "OK"