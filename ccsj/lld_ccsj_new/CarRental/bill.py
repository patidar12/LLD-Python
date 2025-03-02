from reservation import Reservation, ReservationType, ReservationStatus


class Bill:
    def __init__(self, reservation: Reservation):
        self.reservation = reservation
        self.total_bill_amount = self.compute_bill()
        self.is_bill_paid = False
    
    def compute_bill(self):
        if self.reservation.reservation_type == ReservationType.DAILY:
            return self.reservation.vechile.daily_rental_cost
        else:
            return self.reservation.vechile.hourly_rental_cost
    