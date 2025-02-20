from src.config import websocket
from src.dto import socketDto
from src.common.constData import SocketGroup, SocketActionType
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

manager = websocket.getConnectionManager()

async def sendBroadcastWithActionType(group: SocketGroup, actionType: SocketActionType, data):
    jsonResult = socketDto.SocketTypeResponse.of(actionType.value, data).toJson()
    await manager.sendBroadcast(group.value, jsonResult)

async def sendToUserInRoomWithActionType(group: SocketGroup, roomId: int, data):
    jsonResult = socketDto.SocketTypeResponse.of(SocketActionType.AMR.value, data).toJson()
    await manager.sendToUserInRoom(group.value, roomId, jsonResult)