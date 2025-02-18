from fastapi import APIRouter
from src.service import planService
from src.dto import planDto

api = APIRouter()

@api.post("/daily/{fatoryId}", summary="공장 일일 목표치 설정")
def saveDailyPlan(fatoryId: int, saveRequest: planDto.DailyPlanRequest) -> str:
    planService.saveDailyPlan(fatoryId, saveRequest)
    return "OK"