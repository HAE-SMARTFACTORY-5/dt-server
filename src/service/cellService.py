from fastapi import HTTPException
from src.repository import cellRepository
from src.config.database import getDbConnection
from src.dto import cellDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateCell(cellId, request):
    try:
        connection = getDbConnection()

        # amr 존재 확인
        cell = cellRepository.findOrNullById(cellId, connection)
        
        # amr이 존재 X -> 예외
        if cell == None:
            raise HTTPException(status_code=400, detail=f"Cell Not Found. ID: {cellId}")
        
        cellRepository.update(cellId, request, connection)
        connection.commit()
        return cellDto.CellResponse.of(cellId=cellId, source=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateCell() in cellService: {e}")
    finally:
        connection.close

def saveCell(request):
    try:
        connection = getDbConnection()
        cellRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveCell() in cellService: {e}")
    finally:
        connection.close