from fastapi import HTTPException
import mysql.connector

def update(cellId, request, connection):
    query = '''
        UPDATE cell AS c
        SET c.recent_start_time = %s, c.product_id = %s, c.process_status = %s, c.completion_rate = %s
        WHERE c.cell_id = %s
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.recentStartTime, request.productId, request.processStatus, request.completionRate, cellId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error update() in cellRepository: {e}")
    finally:
        cursor.close
        connection.close


def findOrNullById(cellId, connection):
    query = '''
        SELECT *
        FROM cell
        WHERE cell_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [cellId])
        fetch = cursor.fetchall()
        return fetch[0] if fetch else None
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByIdOrNull() in cellRepository: {e}")
    finally:
        cursor.close
        connection.close

def save(request, connection):
    query = '''
        INSERT INTO cell (factory_id, type)
        VALUES (%s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.factoryId, request.cellType])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error save() in cellRepository: {e}")
    finally:
        cursor.close
        connection.close