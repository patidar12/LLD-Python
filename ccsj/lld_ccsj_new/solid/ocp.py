from srp import Invoice
from abc import ABC, abstractmethod

class InvoiceDao(ABC):
    @abstractmethod
    def save(self, invoice: Invoice): pass

class DatabaseInvoiceDao(InvoiceDao):
    def save(self, invoice: Invoice):
        print(f"save invoice: {invoice} to DB")

class FileInvoiceDao(InvoiceDao):
    def save(self, invoice: Invoice):
        print(f"save invoice: {invoice} to File")
