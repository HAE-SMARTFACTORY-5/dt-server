from pydantic import BaseModel
      
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