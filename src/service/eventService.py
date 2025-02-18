from fastapi import HTTPException
from src.repository import eventRepository
from src.config.database import getDbConnection
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveEvent(saveRequest):
    try:
        connection = getDbConnection()
        eventRepository.save(saveRequest, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveEvent() in eventService: {e}")
    finally:
        connection.close

def getElventLogs(eventId, minute):
    try:
        connection = getDbConnection()
        response = eventRepository.findByLogs(eventId, minute, connection)
        connection.commit()
        return response
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error getElventLogs() in eventService: {e}")
    finally:
        connection.close