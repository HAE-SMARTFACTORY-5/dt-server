from fastapi import APIRouter
from service import papercupService
from dto import workerDto

api = APIRouter()

@api.post("/log", summary="작업자 로그 저장")
def saveWokerLog(saveRequest: workerDto.WokerLogRequest) -> str:
    papercupService.saveWorkerLog(saveRequest)
    return "OK"