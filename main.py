from fastapi import FastAPI
from src.router import workerRouter, cellRouter, robotArmRouter, amrRouter, eventRouter, widgetRouter, planRouter
from fastapi.middleware.cors import CORSMiddleware
from src.socket import websocketHandler
import uvicorn  

app = FastAPI()
app.include_router(workerRouter.api, prefix='/worker')
app.include_router(cellRouter.api, prefix='/cell')
app.include_router(robotArmRouter.api, prefix='/robot-arm')
app.include_router(amrRouter.api, prefix='/amr')
app.include_router(eventRouter.api, prefix='/evnet')
app.include_router(widgetRouter.api, prefix='/widget')
app.include_router(planRouter.api, prefix='/plan')

app.add_api_websocket_route("/ws/{typeId}/{clientId}", websocketHandler.websocketEndpoint)

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
    uvicorn.run("main:app --log-config logConfig.yml", host="0.0.0.0", port=8000)
