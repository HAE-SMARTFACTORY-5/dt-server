from fastapi import APIRouter
from src.service import planService
from src.dto import planDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/daily/{fatoryId}", summary="공장 일일 목표치 설정")
def saveDailyPlan(fatoryId: int, saveRequest: planDto.PlanRequest) -> str:
    planService.saveDailyPlan(fatoryId, saveRequest)
    return "OK"

@api.post("/month/{fatoryId}", summary="공장 달별 목표치 설정")
def saveMonthlyPlan(fatoryId: int, saveRequest: planDto.PlanRequest) -> str:
    planService.saveMonthlyPlan(fatoryId, saveRequest)
    return "OK"

@api.patch("/result/{fatoryId}", summary="공장 일일/월별 생산량 업데이트", description="오늘 날짜의 일일/월별 생산량을 1씩 증가시킨다")
async def updateResult(fatoryId: int) -> str:
    result = planService.updateResult(fatoryId)
    jsonResult = socketDto.SocketTypeResponse.of("PLAN", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"

@api.patch("/daily/defect/{fatoryId}", summary="공장 일일 결함 수 업데이트", description="오늘 날짜의 일일 결함수를 1씩 증가시킨다")
async def updateDailtDefect(fatoryId: int) -> str:
    result = planService.updateDailtDefect(fatoryId)
    jsonResult = socketDto.SocketTypeResponse.of("PLAN", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"