'''
We have a marker class having:
    attributes:
        name, color, year, price

For marker class we need to generate invoice for that we have invoice class.

So for that invoice should have marker. It will not extends as invoice don;t have direct relationship with marker.
but invoice can have marker to generate invoice

And to generate invoice , we have to calculatePirce, printINvoice, And save it to DB.

'''

class Marker:
    def __init__(self, name: str, color: str, year: int, price: int):
        self.name: str = name
        self.color: str = color
        self.year: int = year
        self.price: int = price

class Invoice:
    def __init__(self, marker: Marker, quantity: int):
        self.__marker: Marker = marker
        self.__quantity: int = quantity
    
    def calulatePrice(self) -> int:
        price: int = self.__marker.price * self.__quantity
        return price
    
    def printInvoice(self) -> None:
        print("Invoice printed")
    
    def saveToDB(self) -> None:
        print("saved to db")


'''
SRP: single responsibility principle said that 1 class should have 1 responsibility or only one reason to change.

IN above scenario INvoice class can change in 3 scenarion:
 1) calculatePrice: If our price calculation logic changed or we added new field like GST in price calculation.
 2) If our print Invoice logic get changed. we wan't to modify pattern of invoice or design.
 3) if we wan't to update logic to saveINvoice to DB. later if we wan;t to save invoice to File or to cloud(S3).

 Note: for correct implemantation please check srp.py
 
'''