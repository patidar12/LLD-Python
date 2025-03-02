from commands.command import Command
from recevier.ac_conditioner import AcConditioner

class AcTurnOnCommand(Command):
    def __init__(self, ac_conditioner: AcConditioner):
        self.ac = ac_conditioner
    
    def execute(self):
        self.ac.turn_on_ac()

    def undo(self):
        self.ac.turn_of_ac()


class AcTurnOffCommand(Command):
    def __init__(self, ac_conditioner: AcConditioner):
        self.ac = ac_conditioner

    def execute(self):
        self.ac.turn_of_ac()

    def undo(self):
        self.ac.turn_on_ac()
