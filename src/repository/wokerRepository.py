from fastapi import HTTPException
import mysql.connector

def updateWorker(request, connection):
    query = '''
        UPDATE worker AS w
        SET w.cell_id = %s, w.work_status = %s, w.location_x = %s, w.location_y = %s, w.location_z = %s, w.direction = %s
        WHERE w.worker_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.cellId, request.workStatus, request.locationX, request.locationY, request.locationZ,
                               request.direction, request.workerId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateWorker() in workerRepository: {e}")
    finally:
        cursor.close
        connection.close