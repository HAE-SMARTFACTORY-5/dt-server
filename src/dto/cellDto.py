from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CellUpdateRequest(BaseModel):
    cellId: int
    recentStartTime: datetime
    productId: Optional[int] = None
    processStatus: str
    completionRate: Optional[float] = None


#-------------- Response

class CellResponse(BaseModel):
    cellId: Optional[int] = None
    productId: Optional[int] = None
    processStatus: Optional[str] = None
    completionRate: Optional[float] = None

    @classmethod
    def of(cls, row):
        return cls(
                cellId=row['cell_id'],
                productId=row['product_id'],
                processStatus=row['process_status'],
                completionRate=row['completion_rate']
        )
    
    @classmethod
    def withrequest(cls, request: CellUpdateRequest):
        return cls(
                cellId=request.cellId,
                productId=request.productId,
                processStatus=request.processStatus,
                completionRate=request.completionRate
        )