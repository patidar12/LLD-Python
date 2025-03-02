
from Catalog import Product, ProductType
from Cart import ShoppingCart

class EcommerceManager:
    
    def add_product_to_cart(self):
        p1 = Product(name="iphone", price=100000, type=ProductType.ELECTRONIC_GOOD)
        p2 = Product(name="sofa", price=25000, type=ProductType.FURNITURE_GOOD)
        cart = ShoppingCart()
        cart.add_to_cart(p1)
        cart.add_to_cart(p2)
        total_cart_value = cart.get_total_price()
        print(total_cart_value)

EcommerceManager().add_product_to_cart()