from Strategy.SportsDriveStrategy import SportsDriveStrategy
from Vechile import Vechile

class SportsVechile(Vechile):
    def __init__(self):
        super().__init__(SportsDriveStrategy())