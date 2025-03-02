from Strategy.SportsDriveStrategy import SportsDriveStrategy
from Vechile import Vechile

class OffRoadVechile(Vechile):
    def __init__(self):
        super().__init__(SportsDriveStrategy())
