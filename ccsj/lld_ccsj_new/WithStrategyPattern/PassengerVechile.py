from vechile import Vechile
from Strategy.NormalDriveStrategy import NormalDriveStrategy
class PassengerVechile(Vechile):
    def __init__(self):
        super().__init__(NormalDriveStrategy())