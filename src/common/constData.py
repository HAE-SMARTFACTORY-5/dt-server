from enum import Enum

class SocketGroup(Enum):
    FACTORY = "factory"
    AMR = "amr"

class SocketActionType(Enum):
    WORKER = "worker"
    CELL = "cell"
    ROBOT_ARM = "robot-arm"
    ROBOT_ARM_VIBRATION = "robot-arm-vibration"
    AMR = "amr"
    PLAN = "plan"
    #-------
    WORKER_WIDGET = "worker-widget"
    CELL_WIDGET = "cell"
    ROBOT_ARM_WIDGET = "robot-arm-widget"
    AMR_WIDGET = "amr-widget"
    PLAN_WIDGET = "plan-widget"