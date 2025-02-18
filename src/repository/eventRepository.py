from fastapi import HTTPException
import mysql.connector
from src.dto import eventDto, logDto

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

# for 리플레이
def findByLogs(eventId, minute, connection):
    query = '''
        WITH event_filtered AS (
            SELECT DISTINCT created_at
            FROM event
            WHERE created_at BETWEEN created_at - INTERVAL 5 MINUTE AND created_at AND event_id = %s
        ),
        log_union AS (
            SELECT created_at FROM amr_log
            UNION
            SELECT created_at FROM cell_log
            UNION
            SELECT created_at FROM robot_arm_log
        UNION
            SELECT created_at FROM worker_log
        ),
        log_filtered AS (
            SELECT log_union.created_at
            FROM log_union
            JOIN event_filtered ON log_union.created_at BETWEEN event_filtered.created_at - INTERVAL %s MINUTE AND event_filtered.created_at
        )
        SELECT
            lf.created_at,
            amr.amr_id,
            amr.location_x AS amr_location_x,
            amr.location_y AS amr_location_y,
            amr.location_z AS amr_location_z,
            amr.hight,
            amr.direction  AS amr_direction,
            amr.velocity,
            amr.state AS state,
            amr.destination AS destination,
            amr.battery AS battery,
            amr.collision_etected AS collision_etected,
            cell.cell_id,
            cell.product_id,
            cell.process_status,
            cell.completion_rate,
            robot.robot_arm_id,
            robot.location_x AS robot_location_x,
            robot.location_y AS robot_location_y,
            robot.location_z AS robot_location_z,
            robot.direction AS robot_direction,
            robot.angle_1,
            robot.angle_2,
            robot.angle_3,
            worker.worker_id,
            worker.cell_id AS worker_cell_id,
            worker.work_status,
            worker.location_x AS worker_location_x,
            worker.location_y AS worker_location_y,
            worker.location_z AS worker_location_z,
            worker.direction AS worker_direction
        FROM log_filtered lf
            LEFT JOIN amr_log amr ON lf.created_at = amr.created_at
            LEFT JOIN cell_log cell ON lf.created_at = cell.created_at
            LEFT JOIN robot_arm_log robot ON lf.created_at = robot.created_at
            LEFT JOIN worker_log worker ON lf.created_at = worker.created_at
        ORDER BY lf.created_at;
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [eventId, minute])
        results = cursor.fetchall()
        attribute = [
            eventDto.EventLogsData(
                workerLog=logDto.WorkerLogResponse.of(row),
                cellLog=logDto.CellLogResponse.of(row),
                robotArmLog=logDto.RobotArmLogResponse.of(row),
                amrLog=logDto.AmrLogResponse.of(row)
            ) for row in results
        ]
        return eventDto.EventLogsResponse(key=eventId, Value='test', Attributes=attribute)
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error save() in eventRepository: {e}")
    finally:
        cursor.close
        connection.close