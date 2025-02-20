from fastapi import APIRouter
from src.service import worketService
from src.dto import workerDto
from src.config import websocket
from src.socket import websocketService
from src.common.constData import SocketGroup, SocketActionType

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("/{workerId}", summary="작업자 정보 업데이트")
async def updateWoker(workerId: int, request: workerDto.WokerUpdateRequest) -> str:
    workerResponse = worketService.updateWorker(workerId, request)
    websocketService.sendBroadcastWithActionType(SocketGroup.FACTORY, SocketActionType.WORKER, workerResponse)
    return "OK"

@api.post("", summary="작업자 등록")
async def saveWoker(request: workerDto.WokerSaveRequest) -> str:
    worketService.saveWorker(request)
    return "OK"