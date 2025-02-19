from fastapi import HTTPException
from src.repository import logRepository
from src.service import widgetService
from src.config.database import getDbConnection
from src.dto import logDto, widgetDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateWorker(request):
    try:
        connection = getDbConnection()
        logRepository.updateWorker(request, connection)
        connection.commit()
        return logDto.WorkerLogResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveWorkerLog() in logService: {e}")
    finally:
        connection.close

def updateCell(request):
    try:
        connection = getDbConnection()
        logRepository.updateCell(request, connection)
        connection.commit()
        return logDto.CellLogResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveCellLog() in logService: {e}")
    finally:
        connection.close

def updateRobotArm(request):
    try:
        connection = getDbConnection()
        logRepository.updateRobotArm(request, connection)
        connection.commit()
        return logDto.RobotArmLogResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmLog() in logService: {e}")
    finally:
        connection.close

def updateAmr(request):
    try:
        connection = getDbConnection()
        logRepository.updateAmr(request, connection)
        connection.commit()
        return logDto.AmrLogResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveAmrLog() in logService: {e}")
    finally:
        connection.close

def saveRobotArmVibration(saveRequest):
    try:
        connection = getDbConnection()
        logRepository.saveRobotArmVibration(saveRequest, connection)
        connection.commit()
        return widgetService.getRobotArmWidget(saveRequest.robotArmId)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmStatus() in logService: {e}")
    finally:
        connection.close