from fastapi import APIRouter
from src.service import worketService
from src.dto import workerDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="작업자 정보 업데이트")
async def updateWoker(request: workerDto.WokerUpdateRequest) -> str:
    result = worketService.updateWorker(request)
    jsonResult = socketDto.SocketTypeResponse.of("WORKER", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    return "OK"