from fastapi import HTTPException
import mysql.connector

def saveWorkerLog(saveRequest, connection):
    query = '''
        INSERT INTO worker_log (worker_id, cell_id, work_status, location_x, location_y, location_z, direction)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.workerId, saveRequest.cellId, saveRequest.workStatus,
                               saveRequest.locationX, saveRequest.locationY, saveRequest.locationZ, saveRequest.direction])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveWorkerLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

def saveCellLog(saveRequest, connection):
    query = '''
        INSERT INTO cell_log (cell_id, product_id, process_status, completion_rate)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.cellId, saveRequest.productId, saveRequest.processStatus,saveRequest.completionRate])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveCellLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close