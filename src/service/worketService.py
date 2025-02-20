from fastapi import HTTPException
from src.repository import wokerRepository
from src.config.database import getDbConnection
from src.dto import workerDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateWorker(workerId, request):
    try:
        connection = getDbConnection()

        # worker 존재 확인
        worker = wokerRepository.findByIdOrNull(workerId, connection)

        # worker가 존재 X -> 예외
        if worker == None:
            raise HTTPException(status_code=400, detail=f"Worker Not Found. ID: {workerId}")
        
        wokerRepository.update(workerId, request, connection)
        connection.commit()
        return workerDto.WorkerResponse.of(workerId=workerId, source=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateWorker() in workerService: {e}")
    finally:
        connection.close

def saveWorker(request):
    try:
        connection = getDbConnection()
        wokerRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveWorker() in workerService: {e}")
    finally:
        connection.close