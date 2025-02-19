from fastapi import HTTPException
import mysql.connector

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
        raise HTTPException(status_code=500, detail=f"Error updateAmr() in amrRepository: {e}")
    finally:
        cursor.close
        connection.close