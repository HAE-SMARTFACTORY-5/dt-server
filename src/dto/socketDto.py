from pydantic import BaseModel
import json

class SocketTypeResponse(BaseModel):
    actionType: str
    data: dict

    @classmethod
    def of(cls, actionType, data):
        return cls(actionType=actionType, data=data.__dict__)
    
    def toJson(cls):
        return json.dumps(cls.__dict__, ensure_ascii=False)
    
