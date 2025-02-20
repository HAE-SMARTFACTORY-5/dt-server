from fastapi import APIRouter
from src.service import productService
from src.dto import productDto

api = APIRouter()

@api.post("", summary="Product 등록")
async def saveProduct(request: productDto.ProductSaveRequest) -> str:
    productService.saveProduct(request)
    return "OK"

@api.post("/{productId}", summary="Product 정보 수정")
async def updateProduct(productId:int, request: productDto.ProductUpdateRequest) -> str:
    productService.updateProduct(productId, request)
    return "OK"