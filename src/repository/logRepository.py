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

def saveRobotArmLog(saveRequest, connection):
    query = '''
        INSERT INTO robot_arm_log (robot_arm_id, location_x, location_y, location_z, direction, angle_1, angle_2, angle_3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.robotArmId, saveRequest.locationX, saveRequest.locationY, saveRequest.locationZ,
                               saveRequest.direction, saveRequest.angle1, saveRequest.angle2, saveRequest.angle3])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

def saveAmrLog(saveRequest, connection):
    query = '''
        INSERT INTO amr_log (amr_id, location_x, location_y, location_z, hight, direction, speed)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.amrId, saveRequest.locationX, saveRequest.locationY, saveRequest.locationZ,
                               saveRequest.hight, saveRequest.direction, saveRequest.speed])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveAmrLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

def saveRobotArmStatus(saveRequest, connection):
    query = '''
        INSERT INTO robot_arm_status_data (robot_arm_id, fever, electric_current, vibration)
        VALUES (%s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [saveRequest.robotArmId, saveRequest.fever, saveRequest.electricCurrent, saveRequest.vibration])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmStatus() in logRepository: {e}")
    finally:
        cursor.close
        connection.close