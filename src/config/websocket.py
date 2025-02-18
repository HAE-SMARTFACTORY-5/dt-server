from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.rooms: dict[str, dict[str, WebSocket]] = {}  # typeId별 userId-WebSocket 매핑

    async def connect(self, typeId: str, userId: str, websocket: WebSocket):
        await websocket.accept()
        
        # typeId가 없으면 새로 추가
        if typeId not in self.rooms:
            self.rooms[typeId] = {}

        # 해당 typeId 내에 userId를 key로 WebSocket 저장
        self.rooms[typeId][userId] = websocket

    def disconnect(self, typeId: str, userId: str):
        if typeId in self.rooms and userId in self.rooms[typeId]:
            del self.rooms[typeId][userId]

            # 해당 typeId(room)가 비어 있으면 삭제
            if not self.rooms[typeId]:
                del self.rooms[typeId]

    async def sendBroadcastWithOutUserId(self, typeId: str, message: str):
        if typeId in self.rooms:
            for user_id, websocket in self.rooms[typeId].values():
                if user_id != exclude_user: 
                    await websocket.send_text(message)

    async def sendToUserInRoom(self, typeId: str, userId: str, message: str):
        if typeId in self.rooms and str(userId) in self.rooms[typeId]:
            websocket = self.rooms[typeId][str(userId)]
            await websocket.send_text(message)

# 전역 인스턴스 생성
manager = ConnectionManager()

def getConnectionManager():
    return manager
