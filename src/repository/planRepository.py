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

def saveMonthlyPlan(factoryId, saveRequest, connection):
    query = '''
        INSERT INTO monthly_factory_data (factory_id, monthly_total_production_plan, date)
        VALUES (%s, %s, date_format(%s,_utf8mb4'%Y-%m'))
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId, saveRequest.totalProductionPlan, saveRequest.date])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error saveMonthlyPlan() in planRepository: {e}")
    finally:
        cursor.close
        connection.close

def updateDailyResult(factoryId, connection):
    query = '''
        UPDATE daily_factory_data as dfd
        SET dfd.daily_total_production_result = dfd.daily_total_production_result+1
        WHERE dfd.factory_id=%s AND dfd.date=date_format(now(),_utf8mb4'%Y-%m-%d');
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateDailyResult() in planRepository: {e}")
    finally:
        cursor.close
        connection.close

def updateMonthlyResult(factoryId, connection):
    query = '''
        UPDATE monthly_factory_data as mfd
        SET mfd.monthly_total_production_result = mfd.monthly_total_production_result+1
        WHERE mfd.factory_id=%s AND mfd.date=date_format(now(),_utf8mb4'%Y-%m');
    '''
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId])
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error updateMonthlyResult() in planRepository: {e}")
    finally:
        cursor.close
        connection.close