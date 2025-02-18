from fastapi import WebSocket, WebSocketDisconnect
from src.config import websocket

manager = websocket.getConnectionManager()

async def websocketEndpoint(websocket: WebSocket, typeId: str, clientId: str):
    await manager.connect(typeId, clientId, websocket)
    try:
        while True:
            await websocket.receive_text()
            await manager.sendBroadcast(typeId, f"Client {clientId} Connect.")
    except WebSocketDisconnect:
        manager.disconnect(typeId, websocket)
        await manager.sendBroadcast(typeId, f"Client {clientId} Disconnect.")