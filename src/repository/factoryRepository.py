from fastapi import HTTPException
import mysql.connector

def save(request, connection):
    query = '''
        INSERT INTO factory (name)
        VALUES (%s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.name])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error save() in factoryRepository: {e}")
    finally:
        cursor.close
        connection.close