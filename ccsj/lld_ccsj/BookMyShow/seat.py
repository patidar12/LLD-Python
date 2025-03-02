from Enums.seat_category import SeatCategory

class Seat:
    def __init__(self, sid: int, category: SeatCategory, row: int):
        self.id: int = sid
        self.category: SeatCategory = category
        self.row: int = row
