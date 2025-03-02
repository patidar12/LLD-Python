'''
factory that Exctually exposed to client.
'''
from Vechile import Vechile
from SportsVechile import SportsVechile
from GoodsVechile import GoodsVechile
from OffRoadVechile import OffRoadVechile

class VechileDrive:
    def drive(self, vechiles: Vechile):
        for vechile in vechiles:
            vechile.drive()

spV = SportsVechile()
ofrdV = OffRoadVechile()
gdV = GoodsVechile()

vechiles = [spV, ofrdV, gdV]

VechileDrive().drive(vechiles)
