from typing import List

from show import Show
from seat import Seat
from payment import Payment

class Booking:
    def __init__(self, show: Show, booked_seats: List[Seat], payment: Payment):
        self.show: Show = show
        self.booked_seats: List[Seat] = booked_seats
        self.payment: Payment = payment
