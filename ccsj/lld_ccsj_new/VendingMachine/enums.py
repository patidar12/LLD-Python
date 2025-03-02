from enum import Enum

class ItemType(Enum):
    COKE: str = "coke"
    PEPSI: str = "pepsi"
    JUICE: str = "juice"
    SODA: str = "soda"

class Coin(Enum):
    PENNY: int = 1
    NICKEL: int = 5
    DIME: int = 10
    QUARTER: int = 25
