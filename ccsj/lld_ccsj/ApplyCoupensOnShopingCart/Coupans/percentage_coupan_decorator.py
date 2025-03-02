from Coupans import CoupanDecorator
from Catalog import Product

class PercentageCoupanDecorator(CoupanDecorator):
    def __init__(self, product: Product, percentage: int):
        self.product: Product = product
        self.percentage: int =  percentage

    def get_price(self) -> float:
        original_price: float = self.product.get_price()
        discounted_price: float = original_price - ((original_price * self.percentage) / 100)
        return discounted_price

