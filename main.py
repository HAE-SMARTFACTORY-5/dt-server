from fastapi import FastAPI
from src.router import workerRouter, cellRouter, robotArmRouter, amrRouter, eventRouter, widgetRouter, planRouter, productRouter, factoryRouter
from fastapi.middleware.cors import CORSMiddleware
from src.socket import websocketHandler
import uvicorn
import yaml
import os

app = FastAPI()
app.include_router(workerRouter.api, prefix='/worker', tags=["worker"])
app.include_router(cellRouter.api, prefix='/cell', tags=["cell"])
app.include_router(robotArmRouter.api, prefix='/robot-arm', tags=["robot-arm"])
app.include_router(amrRouter.api, prefix='/amr', tags=["amr"])
app.include_router(eventRouter.api, prefix='/evnet', tags=["event"])
app.include_router(widgetRouter.api, prefix='/widget', tags=["widget"])
app.include_router(planRouter.api, prefix='/plan', tags=["plan"])
app.include_router(productRouter.api, prefix='/product', tags=["product"])
app.include_router(factoryRouter.api, prefix='/factory', tags=["factory"])

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
    log_config_path = os.path.abspath("logConfig.yml")
    
    with open(log_config_path, "r") as f:
        log_config = yaml.safe_load(f)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_config=log_config
    )