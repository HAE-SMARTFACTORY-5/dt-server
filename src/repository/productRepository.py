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