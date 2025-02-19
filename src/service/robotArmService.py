from fastapi import HTTPException
from src.repository import robotArmRepository
from src.service import widgetService
from src.config.database import getDbConnection
from src.dto import robotArmDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateRobotArm(request):
    try:
        connection = getDbConnection()
        robotArmRepository.updateRobotArm(request, connection)
        connection.commit()
        return robotArmDto.RobotArmResponse.withrequest(request=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateRobotArm() in robotArmService: {e}")
    finally:
        connection.close

def updateRobotArmVibration(request):
    try:
        connection = getDbConnection()
        robotArmRepository.updateRobotArmVibration(request, connection)
        connection.commit()
        return widgetService.getRobotArmWidget(request.robotArmId)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateRobotArmVibration() in robotArmService: {e}")
    finally:
        connection.close