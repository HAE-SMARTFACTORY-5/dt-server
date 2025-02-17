from fastapi import HTTPException
import mysql.connector
from src.dto import widgetDto

def getTotalWidget(factoryId, connection):
    query = '''
    SELECT *
    FROM factory as f
        LEFT JOIN monthly_factroy_data as mfd ON f.factory_id = mfd.factory_id
        LEFT JOIN daily_factory_data as dfd ON f.factory_id = dfd.factory_id
    WHERE f.factory_id = %s AND STR_TO_DATE(dfd.date, '%Y-%m-%d') = CURDATE();
    ''' 
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, [factoryId])
        result = cursor.fetchone()
        return widgetDto.TotalWidgetResponse.of(result=result)
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Error getTotalWidget() in widgetRepository: {e}")
    finally:
        cursor.close
        connection.close