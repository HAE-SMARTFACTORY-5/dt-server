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
        raise HTTPException(status_code=500, detail=f"Error saveWorkerLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

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
        raise HTTPException(status_code=500, detail=f"Error saveCellLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

def updateRobotArm(request, connection):
    query = '''
        UPDATE robot_arm AS ra
        SET ra.recent_start_time = %s, ra.operating_status = %s, ra.location_x = %s, ra.location_y = %s, ra.location_z = %s, ra.direction = %s, ra.angle_1 = %s, ra.angle_2 = %s, ra.angle_3 = %s
        WHERE ra.robot_arm_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.recentStartTime, request.operatingStatus, request.locationX, request.locationY, request.locationZ,
                               request.direction, request.angle1, request.angle2, request.angle3, request.robotArmId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveRobotArmLog() in logRepository: {e}")
    finally:
        cursor.close
        connection.close

def updateAmr(request, connection):
    query = '''
        UPDATE amr AS a
        SET a.location_x = %s, a.location_y = %s, a.location_z = %s, a.height = %s, a.direction = %s, a.velocity = %s, a.destination = %s, a.battery = %s, a.collision_etected = %s, a.state = %s
        WHERE a.amr_id = %s
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.locationX, request.locationY, request.locationZ,
                               request.height, request.direction, request.velocity, request.destination, request.battery, request.collisionEtected, request.state, request.amrId])
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