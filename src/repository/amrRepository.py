from fastapi import HTTPException
import mysql.connector

def update(amrId, request, connection):
    query = '''
        UPDATE amr AS a
        SET a.type = %s, a.location_x = %s, a.location_y = %s, a.location_z = %s, a.height = %s, a.direction = %s, a.velocity = %s, a.destination = %s, a.battery = %s, a.collision_etected = %s, a.state = %s
        WHERE a.amr_id = %s
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.amrType, request.locationX, request.locationY, request.locationZ,
                               request.height, request.direction, request.velocity, request.destination, request.battery, request.collisionEtected, request.state, amrId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateAmr() in amrRepository: {e}")
    finally:
        cursor.close
        connection.close

def findOrNullById(amrId, connection):
    query = '''
        SELECT *
        FROM amr
        WHERE amr_id = %s;
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [amrId])
        fetch = cursor.fetchall()
        return fetch[0] if fetch else None
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error findByIdOrNull() in amrRepository: {e}")
    finally:
        cursor.close
        connection.close

def save(request, connection):
    query = '''
        INSERT INTO amr (type, location_x, location_y, location_z, height, direction, velocity, destination, battery, collision_etected, state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [request.amrType, request.locationX, request.locationY, request.locationZ,
                               request.height, request.direction, request.velocity, request.destination, request.battery, request.collisionEtected, request.state])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveAmr() in amrRepository: {e}")
    finally:
        cursor.close
        connection.close