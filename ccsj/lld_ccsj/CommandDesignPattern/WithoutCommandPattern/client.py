from devices.ac_conditioner import AcConditioner

class AcRemote:
    def operate_ac(self):
        ac_conditioner: AcConditioner = AcConditioner()
        ac_conditioner.trun_on_ac()
        ac_conditioner.set_temrature(10)
        ac_conditioner.turn_of_ac()


AcRemote().operate_ac()