from enum import Enum

class Location(Enum):
    BANGALORE: str = "bangalore"
    DELHI: str = "delhi"
    MUMBAI: str = "mumbai"


class SeatCategory(Enum):
    SILVER: str = "silver"
    GOLD: str = "gold"
    PLATINUM: str = "platinum"
