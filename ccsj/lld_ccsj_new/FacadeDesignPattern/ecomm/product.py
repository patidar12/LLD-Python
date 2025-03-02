from typing import Dict

class Product: pass

# DAO is data access layer, who intract with actualr DB collection
class ProductDAO:
    def __init__(self):
        self.product: Dict[int, Product] = {}

    def get_product(self, pid):
        print("fetching product details...")
        return self.product.get(pid) or Product() # just for example we are doing like this
