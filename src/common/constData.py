from enum import Enum
from src.common import constData

class SocketGroup(Enum):
    FACTORY = "factory"
    AMR = "amr"

class SocketActionType(Enum):
    WORKER = "worker"
    CELL = "cell"
    ROBOT_ARM = "robot-arm"
    ROBOT_ARM_VIBRATION = "robot-arm-vibration"
    AMR = "amr"
    #-------
    WORKER_WIDGET = "worker-widget"
    CELL_WIDGET = "cell-widget"
    ROBOT_ARM_WIDGET = "robot-arm-widget"
    AMR_WIDGET = "amr-widget"
    PLAN_WIDGET = "plan-widget"

class RobotArmStatus(Enum):
    ACITVE = "ACTIVE"
    INSPECTION = "INACTIVE"
    INACTIVE = "PENDING"

    def __str__(self):
        return {
            "ACTIVE": "정상 운전중",
            "INACTIVE": "비가동중",
            "PENDING": "점검 필요"
        }[self.value]
    