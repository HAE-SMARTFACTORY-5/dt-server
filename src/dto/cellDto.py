from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CellUpdateRequest(BaseModel):
    recentStartTime: datetime
    productId: Optional[int] = None
    processStatus: str
    completionRate: Optional[float] = None

class CellSaveRequest(BaseModel):
    factoryId: int
    cellType: str

#-------------- Response

class CellResponse(BaseModel):
    cellId: Optional[int] = None
    productId: Optional[int] = None
    processStatus: Optional[str] = None
    completionRate: Optional[float] = None

    @classmethod
    def of(cls, cellId, source):
        if isinstance(source, dict):  # `row`가 딕셔너리인 경우
            return cls(
                cellId=cellId,
                productId=source['product_id'],
                processStatus=source['process_status'],
                completionRate=source['completion_rate']
            )
        elif isinstance(source, CellUpdateRequest):  # `request`가 특정 클래스인 경우
            return cls(
                cellId=cellId,
                productId=source.productId,
                processStatus=source.processStatus,
                completionRate=source.completionRate
            )
        else:
            raise TypeError("Invalid argument type. Expected dict or CellUpdateRequest.")
