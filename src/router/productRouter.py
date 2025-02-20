from fastapi import APIRouter
from src.service import productService
from src.dto import productDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="Product 등록")
async def saveProduct(request: productDto.ProductRequest) -> str:
    productService.saveProduct(request)
    return "OK"