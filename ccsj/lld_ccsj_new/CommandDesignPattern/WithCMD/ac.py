class AirConditioner:
    def __init__(self):
        self.is_on: bool = False
        self.temrature: int = 0
    
    def turn_on_ac(self):
        self.is_on = True
        print("AC is turn on...")

    def turn_off_ac(self):
        self.is_on = False
        print("AC is turn off...")
    
    def set_temprature(self, temprature: int):
        self.temrature = temprature
        print(f"Temrature is changes to : {temprature}")
