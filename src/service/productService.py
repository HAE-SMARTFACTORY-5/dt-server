from fastapi import HTTPException
from src.repository import productRepository
from src.config.database import getDbConnection
from src.dto import amrDto
import logging

logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def saveProduct(request):
    try:
        connection = getDbConnection()
        productRepository.save(request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error saveProduct() in productService: {e}")
    finally:
        connection.close