from enum import Enum

class VType(Enum):
    CAR: str = 'car'
    BIKE: str = 'bike'


class VStatus(Enum):
    ACTIVE: str = 'active'
    INACTIVE: str = 'inactive'