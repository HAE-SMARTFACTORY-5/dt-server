from fastapi import WebSocket

class ConnectionManager:
    def __init__(self):
        self.rooms: dict[str, list[WebSocket]] = {}  # typeId를 key로 사용

    async def connect(self, typeId: str, websocket: WebSocket):
        await websocket.accept()
        if typeId not in self.rooms:
            self.rooms[typeId] = []
        self.rooms[typeId].append(websocket)

    def disconnect(self, typeId: str, websocket: WebSocket):
        if typeId in self.rooms:
            self.rooms[typeId].remove(websocket)
            if not self.rooms[typeId]:  # 방이 비어 있으면 삭제
                del self.rooms[typeId]

    async def sendToTypes(self, typeId: str, message: str):
        if typeId in self.rooms:
            for connection in self.rooms[typeId]:
                await connection.send_text(message)

manager = ConnectionManager()
def getConnectionManager():
    return manager