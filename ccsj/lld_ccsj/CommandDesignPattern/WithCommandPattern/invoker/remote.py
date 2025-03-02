from typing import List
from commands.command import Command

class MyRemoteControl:
    command_history: List[Command] = []
    def __init__(self):
        self.command: Command = None
    
    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()
        MyRemoteControl.command_history.append(self.command)

    def undo(self):
        if MyRemoteControl.command_history:
            command: Command = MyRemoteControl.command_history.pop(0)
            command.undo()
