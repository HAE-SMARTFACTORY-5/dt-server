from fastapi import APIRouter
from src.service import cellService, widgetService
from src.dto import cellDto
from src.config import websocket
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/{cellId}", summary="셀 정보 업데이트")
async def updateCell(cellId: int, request: cellDto.CellUpdateRequest) -> str:
    cellResponse = cellService.updateCell(cellId, request)
    cellWidgetReponse = widgetService.getCellWidget(cellId)
    await websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.CELL, cellResponse)
    await websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.CELL_WIDGET, cellWidgetReponse)
    return "OK"

@api.post("", summary="셀 등록")
async def saveCell(request: cellDto.CellSaveRequest) -> str:
    cellService.saveCell(request)
    return "OK"