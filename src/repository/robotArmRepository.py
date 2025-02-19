from fastapi import HTTPException
import mysql.connector

def updateRobotArm(request, connection):
    query = '''
        UPDATE robot_arm AS ra
        SET ra.recent_start_time = %s, ra.operating_status = %s, ra.location_x = %s, ra.location_y = %s, ra.location_z = %s, ra.direction = %s, ra.angle_1 = %s, ra.angle_2 = %s, ra.angle_3 = %s, ra.electric_current = %s, ra.fever = %s
        WHERE ra.robot_arm_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.recentStartTime, request.operatingStatus, request.locationX, request.locationY, request.locationZ,
                               request.direction, request.angle1, request.angle2, request.angle3, request.electric_current, request.fever, request.robotArmId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateRobotArm() in robotArmRepository: {e}")
    finally:
        cursor.close
        connection.close

def updateRobotArmVibration(request, connection):
    query = '''
        INSERT INTO robot_arm_vibration (robot_arm_id, vibration)
        VALUES (%s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.robotArmId, request.vibration])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateRobotArmVibration() in robotArmRepository: {e}")
    finally:
        cursor.close
        connection.close