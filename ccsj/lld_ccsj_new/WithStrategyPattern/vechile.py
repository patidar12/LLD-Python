from Strategy.DriveStrategy import DriveStrategy
class Vechile:
    def __init__(self, drive: DriveStrategy):
        self.drive_strategy: DriveStrategy = drive
    
    def drive(self):
        self.drive_strategy.drive()
