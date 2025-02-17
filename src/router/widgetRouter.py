from fastapi import APIRouter
from src.service import widgetService
from src.dto import widgetDto

api = APIRouter()

@api.get("/total", summary="전체 위젯 조회")
def getTotalWidget(fatoryId: int) -> widgetDto.TotalWidgetResponse:
    return widgetService.getTotalWidget(fatoryId)