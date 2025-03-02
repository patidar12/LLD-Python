class Book:

    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price
    
    def get_name(self) -> str:
        return self.name
    
    def get_price(self) -> float:
        return self.price
