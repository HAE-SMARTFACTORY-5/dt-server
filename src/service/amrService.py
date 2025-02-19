from fastapi import HTTPException
from src.repository import amrRepository
from src.config.database import getDbConnection
from src.dto import amrDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateAmr(request):
    try:
        connection = getDbConnection()
        amrRepository.updateAmr(request, connection)
        connection.commit()
        return amrDto.AmrResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateAmr() in amrService: {e}")
    finally:
        connection.close