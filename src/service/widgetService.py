from fastapi import HTTPException
from src.repository import widgetRepository
from src.config.database import getDbConnection
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