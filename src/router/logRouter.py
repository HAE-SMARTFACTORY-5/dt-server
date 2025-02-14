from fastapi import APIRouter
from service import logService
from dto import logDto

api = APIRouter()

@api.post("/worker", summary="작업자 로그 저장")
def saveWokerLog(saveRequest: logDto.WokerLogRequest) -> str:
    logService.saveWorkerLog(saveRequest)
    return "OK"