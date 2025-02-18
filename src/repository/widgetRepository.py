from fastapi import HTTPException
import mysql.connector
from src.dto import widgetDto

def getTotalWidget(factoryId, connection):
    query = '''
    SELECT *
    FROM factory as f
        LEFT JOIN monthly_factory_data as mfd ON f.factory_id = mfd.factory_id
        LEFT JOIN daily_factory_data as dfd ON f.factory_id = dfd.factory_id
    WHERE f.factory_id = %s AND STR_TO_DATE(dfd.date, '%Y-%m-%d') = CURDATE();
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId])
        result = cursor.fetchall()[0]
        return widgetDto.TotalWidgetResponse.of(result=result)
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getTotalWidget() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close

def getCellWidget(cellId, connection):
    # query = '''
    # SELECT c.cell_id as cell_id,
    #         c.type as type,
    #         c.recent_start_time as recent_start_time,
    #         cl.completion_rate as completion_rate,
    #         cl.process_status as process_status,
    #         p.product_id as product_id,
    #         p.model as model,
    #         p.color as color,
    #         p.process_rate as process_rate,
    #         p.customer_id as customer_id
    # FROM cell as c
    #     LEFT JOIN cell_log as cl ON c.cell_id = cl.cell_id
    #     LEFT JOIN product as p ON p.product_id = cl.product_id
    # WHERE c.cell_id = %s AND cl.created_at = CURDATE();
    # ''' 
    query = '''
    SELECT c.cell_id as cell_id,
            c.type as type,
            c.recent_start_time as recent_start_time,
            c.completion_rate as completion_rate,
            c.process_status as process_status,
            p.product_id as product_id,
            p.model as model,
            p.color as color,
            p.process_rate as process_rate,
            p.customer_id as customer_id
    FROM cell as c
        LEFT JOIN product as p ON p.product_id = c.product_id
    WHERE c.cell_id = %s;
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [cellId])
        return cursor.fetchone()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getCellWidget() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close

def getCellErrorTime(cellId, connection):
    query = '''
        SELECT *
        FROM cell_error_log as cel
        WHERE cel.cell_id = %s AND STR_TO_DATE(cel.start_time, '%Y-%m-%d') = CURDATE();
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [cellId])
        return cursor.fetchall()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getCellWidget() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close

def getRobotArmWidget(robotArmId, connection):
    # query = '''
    #     SELECT *
    #     FROM robot_arm as ra
    #         LEFT JOIN robot_arm_status_data as rasd ON ra.robot_arm_id = rasd.robot_arm_id
    #     WHERE ra.robot_arm_id = %s AND rasd.created_at = NOW();
    # ''' 
    query = '''
        SELECT *
        FROM robot_arm as ra
            LEFT JOIN robot_arm_status_data as rasd ON ra.robot_arm_id = rasd.robot_arm_id
        WHERE ra.robot_arm_id = %s;
    ''' 

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [robotArmId])
        return cursor.fetchall()[0]
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getCellWidget() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close

def getRobotArmVibration(robotArmId, connection):
    # query = '''
    #     SELECT vibration
    #     FROM robot_arm_status_data AS rasd
    #     WHERE rasd.robot_arm_id = %s AND rasd.created_at BETWEEN NOW() - INTERVAL 100 SECOND AND NOW()
    #     ORDER BY rasd.created_at DESC;
    # ''' 
    query = '''
        SELECT vibration
        FROM robot_arm_status_data AS rasd
        WHERE rasd.robot_arm_id = %s AND rasd.created_at BETWEEN NOW() - INTERVAL 100 SECOND AND NOW()
        ORDER BY rasd.created_at DESC;
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [robotArmId])
        results = cursor.fetchall()

        vibration = []
        for row in results:
            vibration.append(row['vibration'])
        return vibration
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getRobotArmVibration() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close