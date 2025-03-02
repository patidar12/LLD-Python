from PassengerVechile import PassengerVechile
from OffRoadVechile import OffRoadVechile
from SportsVechile import SportsVechile
from vechile import Vechile
from typing import List

class VechileManager:
    @staticmethod
    def drive(vechles: List[Vechile]):
        for vechile in vechles:
            vechile.drive()

ps = PassengerVechile()
off = OffRoadVechile()
sprts = SportsVechile()

vechiles = [ps, off, sprts]
VechileManager.drive(vechiles)