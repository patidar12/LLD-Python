from typing import List
from catalog import Product

class ProductCategory:
    def __init__(self, pcid: int, name: str, price: float):
        self.pcid: int = pcid
        self.name: str = name
        self.products: List[Product] = []
        self.price: float = price
    
    def set_price(self, price: float):
        self.price = price
    
    def add_product(self, product: Product):
        self.products.append(product)
    
    def remove_product(self, count: int=1):
        for _ in range(count):
            self.products.remove(0)
