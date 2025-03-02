class Address:
    def __init__(self, pincode: int, city: str, state: str):
        self.pincode: int = pincode
        self.city: str = city
        self.state: str = state
    
    def get_pincode(self):
        return self.pincode
    
    def set_pincode(self, pincode: int):
        self.pincode = pincode

    def get_city(self):
        return self.city

    def set_city(self, city: str):
        self.city = city

    def get_state(self):
        return self.state

    def set_state(self, state: str):
        self.state = state
