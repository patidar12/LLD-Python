from enum import Enum

class OrderStatus(Enum):
    INPROGRESS: int = 1
    DELIVERED: int = 2
    UNDELIVERED: int = 3
    CANCELLED: int = 4
    RETURNED: int = 5
