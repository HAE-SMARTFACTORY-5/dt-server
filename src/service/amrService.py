from fastapi import HTTPException
from src.repository import amrRepository
from src.config.database import getDbConnection
from src.dto import amrDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateAmr(amrId, request):
    try:
        connection = getDbConnection()
        
        # amr 존재 확인
        amr = amrRepository.findByIdOrNull(amrId, connection)
        
        # amr이 존재 X -> 예외
        if amr == None:
            raise HTTPException(status_code=400, detail=f"AMR Not Found. ID: {amrId}")
    
        amrRepository.update(amrId, request, connection)

        connection.commit()
        return amrDto.AmrResponse.of(amrId=amrId, source=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateAmr() in amrService: {e}")
    finally:
        connection.close

def saveAmr(request):
    try:
        connection = getDbConnection()
        amrRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveAmr() in amrService: {e}")
    finally:
        connection.close