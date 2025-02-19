from fastapi import APIRouter
from src.service import amrService
from src.dto import amrDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="AMR 정보 업데이트")
async def updateAmr(request: amrDto.AmrUpdateRequest) -> str:
    result = amrService.updateAmr(request)
    jsonResult = socketDto.SocketTypeResponse.of("AMR", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    await manager.sendToUserInRoom('amr', result.amrId, jsonResult)
    return "OK"