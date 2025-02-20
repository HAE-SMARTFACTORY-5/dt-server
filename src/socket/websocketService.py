from src.config import websocket
from src.dto import socketDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

manager = websocket.getConnectionManager()

async def sendBroadcastWithActionType(group: str, actionType: str, data):
    jsonResult = socketDto.SocketTypeResponse.of(actionType, data).toJson()
    await manager.sendBroadcast(group, jsonResult)

async def sendToUserInRoomWithActionType(group: str, roomId: int, data):
    jsonResult = socketDto.SocketTypeResponse.of("AMR", data).toJson()
    await manager.sendToUserInRoom(group, roomId, jsonResult)