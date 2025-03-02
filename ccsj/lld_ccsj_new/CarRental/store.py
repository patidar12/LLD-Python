from typing import List
from datetime import datetime
from unique_id_generator import UniqueIDGenerator
from vechile_inventory_management import VechileMangementsystem
from reservation import Reservation
from user import User
from product.vechile import Vechile

class Store:
    def __init__(self,
        location):
        self.sid = UniqueIDGenerator.next_id()
        self.location = location
        self.vechle_inv_manager: VechileMangementsystem = VechileMangementsystem()
        self.reservations: List[Reservation] = []
    
    def get_vechiles(self):
        return self.vechle_inv_manager.get_vechiles()
    
    def set_vechiles(self, vechiles):
        self.vechle_inv_manager.add_vechiles(vechiles)

    def create_reservarion(self, user: User, vechile: Vechile):
        self.reservations.append(
            Reservation(
                user,
                vechile,
                datetime.now(),
                datetime.now(),
                datetime.now(),
                self.location,
                self.location
            )
        )

    def complete_reservartion(res_id):
        #take out the reservation from the list and call complete the reservation method.
        return True
