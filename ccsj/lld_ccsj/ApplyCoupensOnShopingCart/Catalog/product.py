from Catalog.product_type import ProductType

class Product:

    def __init__(self, name: str, price: float, type: ProductType):
        self.name: str = name
        self.price: float = price
        self.type: ProductType = type

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type
