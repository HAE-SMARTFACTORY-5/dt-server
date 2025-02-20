from fastapi import APIRouter
from src.service import factoryService
from src.dto import factoryDto

api = APIRouter()

@api.post("", summary="Factory 등록")
async def saveFactory(request: factoryDto.FactorySaveRequest) -> str:
    factoryService.saveFactory(request)
    return "OK"