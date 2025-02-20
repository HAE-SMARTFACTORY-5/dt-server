from fastapi import APIRouter
from src.service import amrService
from src.dto import amrDto, socketDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/{amrId}", summary="AMR 정보 업데이트")
async def updateAmr(amrId: int, request: amrDto.AmrRequest) -> str:
    result = amrService.updateAmr(amrId, request)
    jsonResult = socketDto.SocketTypeResponse.of("AMR", result).toJson()
    await manager.sendBroadcast('factory', jsonResult)
    await manager.sendToUserInRoom('amr', result.amrId, jsonResult)
    return "OK"

@api.post("", summary="AMR 등록")
async def createAmr(request: amrDto.AmrRequest) -> str:
    amrService.saveAmr(request)
    return "OK"