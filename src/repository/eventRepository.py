from fastapi import HTTPException
import mysql.connector

def save(saveRequest, connection):
    query = '''
        INSERT INTO event (worker_id, cell_id, product_id, robot_arm_id, amr_id)
        VALUES (%s, %s, %s, %s, %s)
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.workerId, saveRequest.cellId, saveRequest.productId,
                               saveRequest.robotArmId, saveRequest.amrId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error save() in eventRepository: {e}")
    finally:
        cursor.close
        connection.close