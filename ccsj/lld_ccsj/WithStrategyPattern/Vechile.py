from Strategy.DriveStrategy import DriveStrategy

class Vechile:
    def __init__(self, strategy: DriveStrategy):
        self.strategy = strategy

    def drive(self):
        self.strategy.drive()

