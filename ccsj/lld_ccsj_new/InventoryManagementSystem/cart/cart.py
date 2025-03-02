from typing import Dict

from catalog import ProductCategory

class Cart:
    def __init__(self):
        self.category_id_vs_count_map: Dict[int, int] = {}
    
    def add_item_to_cart(self, category_id: int, count: int):
        if category_id in self.category_id_vs_count_map:
            self.category_id_vs_count_map[category_id] += count
        else:
            self.category_id_vs_count_map[category_id] = count
    
    def remove_item_from_count(self, category_id: int, count: int):
        if category_id in self.category_id_vs_count_map:
            if self.category_id_vs_count_map[category_id] - count <= 0:
                del self.category_id_vs_count_map[category_id]
            else:
                self.category_id_vs_count_map[category_id] -= count

    def empty_cart(self):
        self.category_id_vs_count_map = {}
    
    def get_cart_items(self):
        return self.category_id_vs_count_map
