from typing import List

from Coupans import CoupanDecorator
from Catalog import Product, ProductType

class TypeCoupanDecorator(CoupanDecorator):
    ELIGIBLE_TYPES: List[ProductType] = [ProductType.ELECTRONIC_GOOD, ProductType.FURNITURE_GOOD]
    def __init__(self, product: Product, percentage: int, type: ProductType):
        self.product: Product = product
        self.percentage: int =  percentage
        self.type: ProductType =  type

    def get_price(self) -> float:
        price: float = self.product.get_price()
        if self.type in TypeCoupanDecorator.ELIGIBLE_TYPES:
            price: float = price - ((price * self.percentage) / 100)
        return price
