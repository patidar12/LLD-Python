from typing import List, Dict

from catalog import (
    Product,
    ProductCategory
)

class Invenotry:
    def __init__(self):
        self.product_categories: List[ProductCategory] = []
    

    def add_category(self, pcid: int, pc_name: str, price: float):
        product_category: ProductCategory = ProductCategory(pcid, pc_name, price)
        self.product_categories.append(product_category)
        
    # add product to the particular category
    def add_product(self, product: Product, pc_id: int):
        product_category: ProductCategory = None
        for category in self.product_categories:
            if category.pcid == pc_id:
                product_category = category
                break
        if not product_category:
            raise Exception("NO category found...")
        product_category.add_product(product)
    
    # remove product from the category
    def remove_items(self, product_category_and_count_map: Dict[int, int]):
        for category_id, count in product_category_and_count_map.items():
            category: ProductCategory = self.get_product_category_from_id(category_id)
            category.remove_product(count)

    def get_product_category_from_id(self, pc_id: int):
        for category in self.product_categories:
            if category.pcid == pc_id:
                return category
