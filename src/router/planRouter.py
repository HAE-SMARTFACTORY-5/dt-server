from fastapi import APIRouter
from src.service import planService
from src.dto import planDto

api = APIRouter()

@api.post("/daily/{fatoryId}", summary="공장 일일 목표치 설정")
def saveDailyPlan(fatoryId: int, saveRequest: planDto.PlanRequest) -> str:
    planService.saveDailyPlan(fatoryId, saveRequest)
    return "OK"

@api.post("/month/{fatoryId}", summary="공장 달별 목표치 설정")
def saveMonthlyPlan(fatoryId: int, saveRequest: planDto.PlanRequest) -> str:
    planService.saveMonthlyPlan(fatoryId, saveRequest)
    return "OK"

@api.patch("/daily/result/{fatoryId}", summary="공장 일일 생산량 업데이트", description="오늘 날짜의 일일 생산량을 1씩 증가시킨다")
def saveMonthlyPlan(fatoryId: int) -> str:
    planService.updateDailyResult(fatoryId)
    return "OK"