from Strategy.NormalDriveStrategy import NormalDriveStrategy
from Vechile import Vechile

class GoodsVechile(Vechile):
    def __init__(self):
        super().__init__(NormalDriveStrategy())
