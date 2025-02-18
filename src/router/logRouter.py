from fastapi import APIRouter
from src.service import logService
from src.dto import logDto, socketDto
from src.config import websocket


api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/worker", summary="작업자 로그 저장")
async def saveWokerLog(saveRequest: logDto.WokerUpdateRequest) -> str:
    result = logService.updateWorker(saveRequest)
    jsonResult = socketDto.SocketTypeResponse.of("WORKER", result).toJson()
    await manager.sendBroadcastWithOutUserId('factory', jsonResult)
    return "OK"

@api.post("/cell", summary="셀 로그 저장")
async def saveCellLog(saveRequest: logDto.CellLogRequest) -> str:
    result = logService.updateCell(saveRequest)
    jsonResult = socketDto.SocketTypeResponse.of("CELL", result).toJson()
    await manager.sendBroadcastWithOutUserId('factory', jsonResult)
    return "OK"

@api.post("/robot-arm", summary="로봇 팔 로그 저장")
async def saveRobotArmLog(saveRequest: logDto.RobotArmLogRequest) -> str:
    result = logService.updateRobotArm(saveRequest)
    jsonResult = socketDto.SocketTypeResponse.of("ROBOT-ARM", result).toJson()
    await manager.sendBroadcastWithOutUserId('factory', jsonResult)
    return "OK"

@api.post("/amr", summary="AMR 로그 저장")
async def saveAmrLog(saveRequest: logDto.AmrLogRequest) -> str:
    result = logService.updateAmr(saveRequest)
    jsonResult = socketDto.SocketTypeResponse.of("AMR", result).toJson()
    await manager.sendBroadcastWithOutUserId('factory', jsonResult)
    await manager.sendToUserInRoom('amr', result.amrId, jsonResult)
    return "OK"

@api.post("/robot-arm-status", summary="로봇 팔 상태 저장")
async def saveRobotArmStatus(saveRequest: logDto.RobotArmStatusRequest) -> str:
    result = logService.saveRobotArmStatus(saveRequest)
    jsonResult = socketDto.SocketTypeResponse.of("ROBOT-ARM-STATUS", result).toJson()
    await manager.sendBroadcastWithOutUserId('factory', jsonResult)
    return "OK"