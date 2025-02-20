from fastapi import APIRouter
from src.service import cellService
from src.dto import cellDto
from src.config import websocket
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/{cellId}", summary="셀 정보 업데이트")
async def updateCell(cellId: int, request: cellDto.CellUpdateRequest) -> str:
    cellResponse = cellService.updateCell(cellId, request)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.CELL, cellResponse)
    return "OK"

@api.post("", summary="셀 등록")
async def saveCell(request: cellDto.CellSaveRequest) -> str:
    cellService.saveCell(request)
    return "OK"