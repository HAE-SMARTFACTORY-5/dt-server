from fastapi import HTTPException
import mysql.connector

def saveDailyPlan(factoryId, saveRequest, connection):
    query = '''
        INSERT INTO daily_factory_data (factory_id, daily_total_production_plan, date)
        VALUES (%s, %s, date_format(%s,_utf8mb4'%Y-%m-%d'))
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId, saveRequest.totalProductionPlan, saveRequest.date])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveDailyPlan() in planRepository: {e}")
    finally:
        cursor.close
        connection.close