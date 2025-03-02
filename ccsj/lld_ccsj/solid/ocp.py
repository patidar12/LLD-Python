from srp import Invoice
from abc import ABC, abstractmethod


class InvoiceDao(ABC):
    def __init__(self, invoice: Invoice):
        self.invoice: Invoice = invoice
    
    @abstractmethod
    def save(self):
        pass

class DatabaseInvoiceDao(InvoiceDao):
    def save(self):
        print("save to db")


class FileInvoiceDao(InvoiceDao):
    def save(self):
        print("save to file")

'''
I have created Invoice as abstract class, as we just wan't to giv support of save method for invoice.
But the behaviour is not decided on INvoiceDao level. Like where i have to save the invoice to Database or File Or CLoud
I have made the save method as abstract so all the child class need to implement the save method.
DatabaseInvoiceDao, FileInvoiceDao can extends InvoiceDao and implement the functionality in save method.

We can use interface also here.
1) INcoiceDao itself provide implemenatation of save method to save invoice in DB.
2) DatabaseInvoiceDao just extends the invoiceDao class.
3) FileInvoiceDao extends invoiceDao class and override the save method.

But as i thought i invoiceDao provide the functionality to save info to database for that it can be creating the db connection ans other things.
So when the FileInvoiceDao extends that creating db connection code is extended by FileInvoiceDao by default that is irrelavlant to FileInvoiceDao.
So i thought of creating a abstrace class and ask base class to implement the save method, acoording to their use case. 

TODO: Interfaces can be implemented differently in python. Ned to dive deep.
'''
