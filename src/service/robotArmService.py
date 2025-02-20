from fastapi import HTTPException
from src.repository import robotArmRepository
from src.service import widgetService
from src.config.database import getDbConnection
from src.dto import robotArmDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def updateRobotArm(robotArmId, request):
    try:
        connection = getDbConnection()
        
        # robot-arm 존재 확인
        robotArm = robotArmRepository.findOrNullById(robotArmId, connection)

        # amr이 존재 X -> 예외
        if robotArm == None:
            raise HTTPException(status_code=400, detail=f"Robot Arm Not Found. ID: {robotArmId}")
        
        robotArmRepository.update(robotArmId, request, connection)
        connection.commit()
        return robotArmDto.RobotArmResponse.of(robotArmId=robotArmId, source=request)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateRobotArm() in robotArmService: {e}")
    finally:
        connection.close

def saveRobotArm(request):
    try:
        connection = getDbConnection()
        robotArmRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveRobotArm() in robotArmService: {e}")
    finally:
        connection.close

def saveRobotArmVibration(romotArmId, request):
    try:
        connection = getDbConnection()
        robotArmRepository.saveRobotArmVibration(romotArmId, request, connection)
        connection.commit()
        return widgetService.getRobotArmWidget(romotArmId)
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateRobotArmVibration() in robotArmService: {e}")
    finally:
        connection.close