from fastapi import APIRouter
from src.service import eventService
from src.dto import eventDto
from typing import Dict

api = APIRouter()

@api.post("", summary="에러 이벤트 저장")
def saveEvent(saveRequest: eventDto.SaveRequest) -> str:
    eventService.saveEvent(saveRequest)
    return "OK"

@api.get("/logs", summary="이벤트와 관련된 로그 조회", description="minute는 event 발생 기점으로 n분전의 데이터부터 조회")
def getEventLogs(eventId: int, minute: int = 5) -> Dict[str, eventDto.EventLogsResponse]:
    data = eventService.getElventLogs(eventId, minute)
    return {'data': data}