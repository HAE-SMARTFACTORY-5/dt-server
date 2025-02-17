from pydantic import BaseModel
from typing import Optional
      
class TotalWidgetResponse(BaseModel):
    factoryId: int
    monthlyPlan: int
    monthlyResult: int
    dailyPlan: int
    dailyResult: int
    defectiveQualityCount: int
    date: str

    @classmethod
    def of(cls, result):
        return cls(
                factoryId=result['factory_id'],
                monthlyPlan=result['monthly_total_production_plan'],
                monthlyResult=result['monthly_total_production_result'],
                dailyPlan=result['daily_total_production_plan'],
                dailyResult=result['daily_total_production_result'],
                defectiveQualityCount=result['defective_quality_count'],
                date=result['date']
        )
    
class CellWidgetResponse(BaseModel):
    cellId: Optional[int] = None
    cellType: Optional[str] = None
    startTime: Optional[str] = None
    processTime: Optional[str] = None
    processStatus: Optional[str] = None
    completionRate: Optional[float] = None
    processRate: Optional[float] = None
    productId: Optional[int] = None
    productModel: Optional[str] = None
    productColor: Optional[str] = None
    productProcessRate: Optional[float] = None
    customerId: Optional[str] = None

    @classmethod
    def of(cls, result, processTime, cellProcessRate):
        if result == None:
            return cls(
            cellId=None,
            cellType=None,
            startTime=None,
            processTime=None,
            processStatus=None,
            completionRate=None,
            processRate=cellProcessRate,
            productId=None,
            productModel=None,
            productColor=None,
            productProcessRate=None,
            customerId=None
            )
        return cls(
            cellId=result['cell_id'],
            cellType=result['type'],
            startTime=str(result['recent_start_time']),
            processTime=str(int(processTime.total_seconds()/60)),
            processStatus=result['process_status'],
            completionRate=result['completion_rate'],
            processRate=cellProcessRate,
            productId=result['product_id'],
            productModel=result['model'],
            productColor=result['color'],
            productProcessRate=result['process_rate'],
            customerId=result['customer_id']
        )
    
class RobotArmWidgetResponse(BaseModel):
    robotArmId: Optional[int] = None
    recentStartTime: Optional[str] = None
    processTime: Optional[int] = None
    operatingStatus: Optional[str] = None
    fever: Optional[float] = None
    electricCurrent: Optional[float] = None
    vibration: Optional[list] = None

    @classmethod
    def of(cls, result, processTime, vibration):
        if result == None:
            return cls(
                robotArmId=None,
                recentStartTime=None,
                processTime=None,
                operatingStatus=None,
                fever=None,
                electricCurrent=None,
                vibration=None
            )
        
        return cls(
            robotArmId=result['robot_arm_id'],
            recentStartTime=str(result['recent_start_time']),
            processTime=str(int(processTime.total_seconds()/60)),
            operatingStatus=result['operating_status'],
            fever=result['fever'],
            electricCurrent=result['electric_current'],
            vibration=vibration
        )