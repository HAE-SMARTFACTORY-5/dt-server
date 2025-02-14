from fastapi import APIRouter
from src.service import eventService
from src.dto import eventDto

api = APIRouter()

@api.post("", summary="작업자 로그 저장")
def saveEvent(saveRequest: eventDto.SaveRequest) -> str:
    eventService.saveEvent(saveRequest)
    return "OK"