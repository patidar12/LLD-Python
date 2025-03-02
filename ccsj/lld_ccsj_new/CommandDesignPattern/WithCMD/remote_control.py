from typing import List
from command.command import ICommand

class MyRemoteControl:
    def __init__(self):
        self.command: ICommand = None
        self.operations: List[ICommand] = []
    
    def set_command(self, command: ICommand):
        self.command = command
    
    def press_button(self):
        self.command.execute()
        self.operations.append(self.command)

    def undo(self):
        if self.operations:
            cmd = self.operations.pop(-1)
            cmd.undo()
