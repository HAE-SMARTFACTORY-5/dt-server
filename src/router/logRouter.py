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