class Bulb:
    def __init__(self):
        self.is_on: bool = False
    
    def turn_on(self):
        self.is_on = True
        print("Bulb is turn on...")

    def turn_off(self):
        self.is_on = False
        print("Bulb is turn off...")

