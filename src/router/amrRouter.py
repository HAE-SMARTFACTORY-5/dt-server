from fastapi import APIRouter
from src.service import amrService
from src.dto import amrDto, socketDto
from src.config import websocket
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/{amrId}", summary="AMR 정보 업데이트")
async def updateAmr(amrId: int, request: amrDto.AmrRequest) -> str:
    amrResponse = amrService.updateAmr(amrId, request)
    await websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.AMR, amrResponse)
    await websocketService.sendToUserInRoomWithActionType(SocketGroup.AMR, amrId, amrResponse)
    return "OK"

@api.post("", summary="AMR 등록")
async def createAmr(request: amrDto.AmrRequest) -> str:
    amrService.saveAmr(request)
    return "OK"