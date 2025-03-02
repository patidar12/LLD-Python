from ac import AirConditioner
from command.turn_on_ac_cmd import TurnOnAcCMD
from command.turn_off_ac_cmd import TurnOffAcCMD
from remote_control import MyRemoteControl

class Remote:
    def execute_cmd(self):
        ac: AirConditioner = AirConditioner()
        turn_on_ac: TurnOnAcCMD = TurnOnAcCMD(ac)
        remote: MyRemoteControl = MyRemoteControl()
        remote.set_command(turn_on_ac)
        remote.press_button()
        remote.undo()

Remote().execute_cmd()