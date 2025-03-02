from enums import SeatCategory

class Seat:
    def __int__(self, row, number, category: SeatCategory, price):
        self.row = row
        self.category = category
        self.price = price
        self.number = number
