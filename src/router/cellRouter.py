from fastapi import APIRouter
from src.service import cellService
from src.dto import cellDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="셀 정보 업데이트")
async def updateCell(request: cellDto.CellUpdateRequest) -> str:
    result = cellService.updateCell(request)
    jsonResult = socketDto.SocketTypeResponse.of("CELL", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"