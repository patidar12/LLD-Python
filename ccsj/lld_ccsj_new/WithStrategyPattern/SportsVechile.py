from vechile import Vechile
from Strategy.SpecialDriveStrategy import SpecialDriveStrategy
class SportsVechile(Vechile):
    def __init__(self):
        super().__init__(SpecialDriveStrategy())
