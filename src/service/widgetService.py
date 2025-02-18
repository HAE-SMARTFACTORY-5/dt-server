from fastapi import HTTPException
from src.repository import widgetRepository
from src.dto import widgetDto
from src.config.database import getDbConnection
from datetime import datetime
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def getTotalWidget(fatoryId):
    try:
        connection = getDbConnection()
        response = widgetRepository.getTotalWidget(fatoryId, connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error getTotalWidget() in widgetService: {e}")
    finally:
        connection.close

def getCellWidget(cellId):
    try:
        connection = getDbConnection()
        result = widgetRepository.getCellWidget(cellId, connection)
        errorTimes = widgetRepository.getCellErrorTime(cellId, connection)
        current_time = datetime.now()

        # 현재 실행중인 시간
        cellProcessTime = None
        cellErrorTime = None
        cellProcessRate = None
        if result != None:
            cellProcessTime = current_time - result['recent_start_time']

            # Error 발생했던 시간
            cellErrorTime = cellProcessTime
            for errorTime in errorTimes:
                if errorTime['end_time'] != None:
                    cellErrorTime -= errorTime['end_time'] - errorTime['start_time']
                else:
                    cellErrorTime -= current_time - errorTime['start_time']

            cellProcessRate=(cellErrorTime/cellProcessTime)*100
        
        connection.commit()
        return widgetDto.CellWidgetResponse.of(result=result, processTime=cellProcessTime, cellProcessRate=cellProcessRate)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error getCellWidget() in widgetService: {e}")
    finally:
        connection.close

def getRobotArmWidget(robotArmId):
    try:
        connection = getDbConnection()
        result = widgetRepository.getRobotArmWidget(robotArmId, connection)
        current_time = datetime.now()
        # 현재 실행중인 시간
        processTime = None
        if result != None:
            processTime = current_time - result['recent_start_time']

        vibration = widgetRepository.getRobotArmVibration(robotArmId, connection)
        
        connection.commit()
        return widgetDto.RobotArmWidgetResponse.of(result=result, processTime=processTime, vibration=vibration)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error getRobotArmWidget() in widgetService: {e}")
    finally:
        connection.close