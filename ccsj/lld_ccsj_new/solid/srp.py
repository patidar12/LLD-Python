class Marker:
    def __init__(self, name, color, year, price):
        self.name = name
        self.color = color
        self.year = year
        self.price = price


class Invoice:
    def __init__(self, marker: Marker, quantity: int):
        self.__marker: Marker = marker
        self.__quantity: int = quantity
    
    def calculate_total(self):
        price = self.__marker.price * self.__quantity
        return price
    

class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.__invoice: Invoice = invoice
    
    def save_to_db(self):
        print("save data to db")

class InvoicePrinter:
    def __init__(self, invoice: Invoice):
        self.__invoice: Invoice = invoice

    def print(self):
        print("printing invoice!")
