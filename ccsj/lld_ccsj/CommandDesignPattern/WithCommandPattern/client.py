from recevier.ac_conditioner import AcConditioner
from invoker.remote import MyRemoteControl
from commands.ac_command import AcTurnOffCommand, AcTurnOnCommand

class AcRemote:
    def operate_ac(self):
        # create Ac
        ac: AcConditioner = AcConditioner()
        ac_on_command = AcTurnOnCommand(ac)
        remote: MyRemoteControl = MyRemoteControl()
        remote.set_command(ac_on_command)
        remote.press_button()
        remote.press_button()
        ac_off_command = AcTurnOffCommand(ac)
        remote.set_command(ac_off_command)
        remote.press_button()
        remote.press_button()
        print(f"\n")
        print(f"Undo above operations..\n")
        remote.undo()
        remote.undo()
        remote.undo()

AcRemote().operate_ac()
