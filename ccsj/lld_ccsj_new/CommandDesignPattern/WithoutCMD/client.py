from air_conditioner import AirConditioner
from bulb import Bulb

class Remote:
    def execute_cmd(self):
        ac = AirConditioner()
        ac.turn_on_ac()
        ac.set_temprature(20)
        ac.turn_off_ac()

        bulb = Bulb()
        bulb.turn_on()
        bulb.turn_off()


Remote().execute_cmd()