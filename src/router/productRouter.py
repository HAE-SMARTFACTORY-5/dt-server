from fastapi import APIRouter
from src.service import productService
from src.dto import productDto
from src.config import websocket

api = APIRouter()
manager = websocket.getConnectionManager()

@api.post("", summary="Product 등록")
async def saveProduct(request: productDto.ProductSaveRequest) -> str:
    productService.saveProduct(request)
    return "OK"

@api.post("/{productId}", summary="Product 정보 수정")
async def updateProduct(productId:int, request: productDto.ProductUpdateRequest) -> str:
    productService.updateProduct(productId, request)
    return "OK"