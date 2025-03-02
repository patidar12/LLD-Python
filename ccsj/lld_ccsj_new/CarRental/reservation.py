from enum import Enum
from unique_id_generator import UniqueIDGenerator
from user import User
from product.vechile import Vechile

class ReservationType(Enum):
    HOURLY: str = "hourly"
    DAILY: str = "daily"

class ReservationStatus(Enum):
    SCHEDULED: str = "scheduled"
    INPROGRESS: str = "inprogress"
    COMPLETED: str = "completed"
    CANCELLED: str = "cancled"


class Reservation:
    def __init__(
            self,
            user: User,
            vechile: Vechile,
            booking_date,
            booked_from,
            booked_till,
            pickup_location,
            drop_location,
            reservation_type: ReservationType = ReservationType.DAILY,
            reservation_status: ReservationStatus = ReservationStatus.INPROGRESS
            ):
        self.rid = UniqueIDGenerator.next_id()
        self.user: User = user
        self.vechile: Vechile = vechile
        self.booking_date = booking_date
        self.booked_from = booked_from
        self.booked_till = booked_till
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.reservation_type: ReservationType = reservation_type
        self.reservation_status: ReservationStatus = reservation_status
