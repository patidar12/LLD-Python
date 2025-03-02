class Marker:
    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price


class Invoice:
    def __init__(self, marker: Marker, quantity: int):
        self.marker: Marker = marker
        self.quantity: int = quantity
    
    def calculate_total(self):
        price = self.marker.price * self.quantity
        return price
    
    def print_invoice(self):
        print("printing invoice!")
    
    def save_to_db(self):
        print("save data to db")

