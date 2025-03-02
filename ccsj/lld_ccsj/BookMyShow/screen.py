from typing import List
from seat import Seat

class Screen:
    def __init__(self, sid: int, seats: List[Seat]):
        self.id: int = sid
        self.seats: List[Seat] = seats
