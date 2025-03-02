from srp import Invoice


class InvoiceDao:
    def __init__(self, invoice: Invoice):
        self.__invoice: Invoice = invoice
    
    def save_to_db(self):
        print("save data to db")

    def save_to_file(self, file_name):
        print(f"Save ata to file: {file_name}") 

