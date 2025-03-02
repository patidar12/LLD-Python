class AcConditioner:
    def __init__(self):
        self.is_on: bool = False
        self.temrature: int = 0
    
    def turn_on_ac(self):
        self.is_on = True
        print("Ac turned on")
    
    def turn_of_ac(self):
        self.is_on = False
        print("Ac turned off")
    
    def set_temrature(self, temrature: int):
        self.temrature = temrature
        print("Temrature: ", temrature)
    