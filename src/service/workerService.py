from fastapi import HTTPException
from src.repository import workerRepository
from src.config.database import getDbConnection
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveWorkerLog(saveRequest):
    try:
        connection = getDbConnection()
        workerRepository.save(saveRequest, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error savePapercup() in papercupService: {e}")
    finally:
        connection.close