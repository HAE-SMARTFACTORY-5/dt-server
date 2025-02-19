from fastapi import HTTPException
from src.repository import wokerRepository
from src.config.database import getDbConnection
from src.dto import workerDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateWorker(request):
    try:
        connection = getDbConnection()
        wokerRepository.updateWorker(request, connection)
        connection.commit()
        return workerDto.WorkerResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateWorker() in workerService: {e}")
    finally:
        connection.close