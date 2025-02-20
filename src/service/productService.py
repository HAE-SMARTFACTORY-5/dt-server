from fastapi import HTTPException
from src.repository import productRepository
from src.config.database import getDbConnection
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

def updateProduct(productId, request):
    try:
        connection = getDbConnection()

        # product 존재 확인
        product = productRepository.findOrNullById(productId, connection)
        
        # amr이 존재 X -> 예외
        if product == None:
            raise HTTPException(status_code=400, detail=f"Cell Not Found. ID: {productId}")
        
        productRepository.update(productId, request, connection)
        connection.commit()
    except Exception as e:
        connection.rollback()
        logging.error(e)
        raise HTTPException(status_code=500, detail=f"Error updateProduct() in productService: {e}")
    finally:
        connection.close