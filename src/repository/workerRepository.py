from fastapi import HTTPException
import mysql.connector

def save(saveRequest, connection):
    query = '''
        INSERT INTO worker_log (worker_id, cell_id, work_status, location_x, location_y, location_z, direction)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.workerId, saveRequest.cellId, saveRequest.workStatus,
                               saveRequest.locationX, saveRequest.locationY, saveRequest.locationZ, saveRequest.direction])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByPapercupId(): {e}")
    finally:
        cursor.close
        connection.close