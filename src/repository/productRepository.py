from fastapi import HTTPException
import mysql.connector

def save(request, connection):
    query = '''
        INSERT INTO product (customer_id, model, color)
        VALUES (%s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.customerId, request.model, request.color])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error save() in productRepository: {e}")
    finally:
        cursor.close
        connection.close

def update(productId, request, connection):
    query = '''
        UPDATE product AS p
        SET p.amr_id = %s, p.product_status = %s, process_rate = %s
        WHERE p.product_id = %s
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.amrId, request.productStatus, request.processRate, productId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error update() in productRepository: {e}")
    finally:
        cursor.close
        connection.close


def findOrNullById(productId, connection):
    query = '''
        SELECT *
        FROM product
        WHERE product_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [productId])
        fetch = cursor.fetchall()
        return fetch[0] if fetch else None
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByIdOrNull() in productRepository: {e}")
    finally:
        cursor.close
        connection.close