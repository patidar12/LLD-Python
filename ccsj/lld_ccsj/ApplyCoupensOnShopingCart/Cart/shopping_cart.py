from typing import List

from Catalog import Product
from Coupans import PercentageCoupanDecorator, TypeCoupanDecorator

class ShoppingCart:
    def __init__(self):
        self.products: List[Product] = []    

    def add_to_cart(self, product: Product):
        # we can add according to logic of coupan apply.
        product_with_discount: Product = TypeCoupanDecorator(
            PercentageCoupanDecorator(product=product, percentage=10), # this is itself a product as CoupanDecorator is a subclass of product
            percentage=10,
            type=product.get_type()
        )
        self.products.append(product_with_discount)

    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products:
            total_price += product.get_price()
        return total_price
