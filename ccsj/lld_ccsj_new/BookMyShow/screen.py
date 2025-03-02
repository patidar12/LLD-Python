from typing import List
from seat import Seat

class Screen:
    def __init__(self, sid: int, seats: List[Seat]):
        self.sid: int = sid
        self.seats: List[Seat] = seats
