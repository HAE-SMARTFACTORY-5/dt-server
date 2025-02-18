from fastapi import APIRouter
from src.service import widgetService
from src.dto import widgetDto

api = APIRouter()

@api.get("/total", summary="전체 위젯 조회")
def getTotalWidget(fatoryId: int) -> widgetDto.TotalWidgetResponse:
    response = widgetService.getTotalWidget(fatoryId)
    print("dd??c")
    return response

@api.get("/cell", summary="셀 위젯 조회", description="processTime는 분단위")
def getCellWidget(cellId: int) -> widgetDto.CellWidgetResponse:
    return widgetService.getCellWidget(cellId)

@api.get("/robot-arm", summary="설비 위젯 조회")
def getRobotArmWidget(robotArmId: int) -> widgetDto.RobotArmWidgetResponse:
    return widgetService.getRobotArmWidget(robotArmId)