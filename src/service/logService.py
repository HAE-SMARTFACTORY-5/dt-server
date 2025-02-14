from fastapi import HTTPException
from src.repository import logRepository
from src.config.database import getDbConnection
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveWorkerLog(saveRequest):
    try:
        connection = getDbConnection()
        logRepository.saveWorkerLog(saveRequest, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveWorkerLog() in logService: {e}")
    finally:
        connection.close

def saveCellLog(saveRequest):
    try:
        connection = getDbConnection()
        logRepository.saveCellLog(saveRequest, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveCellLog() in logService: {e}")
    finally:
        connection.close

def saveRobotArmLog(saveRequest):
    try:
        connection = getDbConnection()
        logRepository.saveRobotArmLog(saveRequest, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmLog() in logService: {e}")
    finally:
        connection.close