from fastapi import HTTPException
from src.repository import cellRepository
from src.config.database import getDbConnection
from src.dto import cellDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateCell(request):
    try:
        connection = getDbConnection()
        cellRepository.updateCell(request, connection)
        connection.commit()
        return cellDto.CellResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateCell() in cellService: {e}")
    finally:
        connection.close