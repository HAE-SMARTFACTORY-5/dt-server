from fastapi import APIRouter
from src.service import workerService
from src.dto import workerDto

api = APIRouter()

@api.post("/log", summary="작업자 로그 저장")
def saveWokerLog(saveRequest: workerDto.WokerLogRequest) -> str:
    workerService.saveWorkerLog(saveRequest)
    return "OK"