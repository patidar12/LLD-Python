from typing import List
from store import Store
from user import User

class VehicleRentalSystem:
    def __init__(self, stores: List[Store], users: List[User]):
        self.stores = stores
        self.users = users
    
    def get_store(self):
        # based on location, we will filter out the Store from storeList.
        return self.stores[0]

    # addUsers

    # remove users


    # add stores

    # remove stores

