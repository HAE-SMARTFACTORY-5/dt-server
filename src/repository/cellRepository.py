from fastapi import HTTPException
import mysql.connector

def updateCell(request, connection):
    query = '''
        UPDATE cell AS c
        SET c.recent_start_time = %s, c.product_id = %s, c.process_status = %s, c.completion_rate = %s
        WHERE c.cell_id = %s
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.recentStartTime, request.productId, request.processStatus, request.completionRate, request.cellId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateCell() in cellRepository: {e}")
    finally:
        cursor.close
        connection.close