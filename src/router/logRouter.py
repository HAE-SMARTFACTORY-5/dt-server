from fastapi import APIRouter
from src.service import logService
from src.dto import logDto

api = APIRouter()

@api.post("/worker", summary="작업자 로그 저장")
def saveWokerLog(saveRequest: logDto.WokerLogRequest) -> str:
    logService.saveWorkerLog(saveRequest)
    return "OK"

@api.post("/cell", summary="셀 로그 저장")
def saveCellLog(saveRequest: logDto.CellLogRequest) -> str:
    logService.saveCellLog(saveRequest)
    return "OK"

@api.post("/robot-arm", summary="로봇 팔 로그 저장")
def saveRobotArmLog(saveRequest: logDto.RobotArmLogRequest) -> str:
    logService.saveRobotArmLog(saveRequest)
    return "OK"

@api.post("/amr", summary="AMR 로그 저장")
def saveAmrLog(saveRequest: logDto.AmrLogRequest) -> str:
    logService.saveAmrLog(saveRequest)
    return "OK"

@api.post("/robot-arm-status", summary="로봇 팔 상태 저장")
def saveRobotArmStatus(saveRequest: logDto.RobotArmStatusRequest) -> str:
    logService.saveRobotArmStatus(saveRequest)
    return "OK"