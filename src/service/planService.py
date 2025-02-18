from fastapi import HTTPException
from src.repository import planRepository
from src.config.database import getDbConnection
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveDailyPlan(fatoryId, saveRequest):
    try:
        connection = getDbConnection()
        response = planRepository.saveDailyPlan(fatoryId, saveRequest, connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveDailyPlan() in planService: {e}")
    finally:
        connection.close

def saveMonthlyPlan(fatoryId, saveRequest):
    try:
        connection = getDbConnection()
        response = planRepository.saveMonthlyPlan(fatoryId, saveRequest, connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveMonthPlan() in planService: {e}")
    finally:
        connection.close