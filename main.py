from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from src.router import logRouter, eventRouter, widgetRouter, planRouter
from fastapi.middleware.cors import CORSMiddleware
from src.config import websocket
import uvicorn  

app = FastAPI()
app.include_router(logRouter.api, prefix='/log')
app.include_router(eventRouter.api, prefix='/evnet')
app.include_router(widgetRouter.api, prefix='/widget')
app.include_router(planRouter.api, prefix='/plan')


manager = websocket.getConnectionManager()

@app.websocket("/ws/{typeId}/{clientId}")
async def websocketEndpoint(websocket: WebSocket, typeId: str, clientId: str):
    await manager.connect(typeId, clientId, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.sendBroadcastWithOutUserId(typeId, f"Client {clientId} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(typeId, websocket)
        await manager.sendBroadcastWithOutUserId(typeId, f"Client {clientId} Disconnect.")

# CORS 설정
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)