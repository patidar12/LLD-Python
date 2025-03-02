from enum import Enum

class ExpenseSplitType(Enum):
    EQUAL: str = "equal"
    UNEQUAL: str = "unequal"
    PERCENTAGE: str = "percentage"