#from typing import final
from abc import ABC, abstractmethod, ABCMeta
from runtime_final import final

class PaymentFlow(metaclass=ABCMeta):
    @abstractmethod
    def validate_request(self):
        pass
    @abstractmethod
    def debit_amount(self):
        pass
    @abstractmethod
    def calculate_fees(self):
        pass
    @abstractmethod
    def credit_amount(self):
        pass

    # template method, that decide order of steps. And it will be same for all the child class.
    # ths can't be overriden as we are making it final.
    # However child classes can implement the steps logic.
    @final
    def send_money(self):
        self.validate_request()
        self.debit_amount()
        self.calculate_fees()
        self.credit_amount()

