from fastapi import APIRouter
from src.service import planService
from src.dto import planDto, socketDto
from src.config import websocket
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

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
    planResponse = planService.updateResult(fatoryId)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.PLAN_WIDGET, planResponse)
    return "OK"

@api.patch("/daily/defect/{fatoryId}", summary="공장 일일 결함 수 업데이트", description="오늘 날짜의 일일 결함수를 1씩 증가시킨다")
async def updateDailtDefect(fatoryId: int) -> str:
    planResponse = planService.updateDailtDefect(fatoryId)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.PLAN_WIDGET, planResponse)
    return "OK"