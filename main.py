from fastapi import FastAPI
from src.router import logRouter, eventRouter, widgetRouter
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()
app.include_router(logRouter.api, prefix='/log')
app.include_router(eventRouter.api, prefix='/evnet')
app.include_router(widgetRouter.api, prefix='/widget')

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