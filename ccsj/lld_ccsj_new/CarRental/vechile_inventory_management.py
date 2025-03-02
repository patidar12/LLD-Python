from typing import List
from product.vechile import Vechile

class VechileMangementsystem:
    def __init__(self):
        self.vehciles: List[Vechile] = []
    
    def add_vechiles(self, vechile: List[Vechile]):
        self.vehciles.extend(vechile)
    
    def remove_vehcile(self, vechile: Vechile):
        self.vehciles.remove(vechile)
    
    def get_vechiles(self):
        return self.vehciles
    