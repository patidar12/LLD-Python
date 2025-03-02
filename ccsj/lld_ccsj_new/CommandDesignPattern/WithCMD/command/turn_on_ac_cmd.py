from command.command import ICommand
from ac import AirConditioner

class TurnOnAcCMD(ICommand):
    def __init__(self, ac: AirConditioner):
        self.ac: AirConditioner = ac
    
    def execute(self):
        self.ac.turn_on_ac()
    

    def undo(self):
        self.ac.turn_off_ac()
