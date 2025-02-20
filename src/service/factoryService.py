from fastapi import HTTPException
from src.repository import factoryRepository
from src.config.database import getDbConnection
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveFactory(request):
    try:
        connection = getDbConnection()
        factoryRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveFactory() in factoryRepository: {e}")
    finally:
        connection.close