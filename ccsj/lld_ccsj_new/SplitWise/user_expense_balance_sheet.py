from typing import Dict, List

from user import User
from balance import Balance

class UserExpenseBalanceSheet:
    def __init__(self):
        self.user_vs_balance: Dict[str, Balance] = {}
        self.total_your_expense = 0
        self.total_payment = 0
        self.total_you_owe = 0
        self.total_you_get_back = 0 
    
    def get_user_vs_balance(self):
        return self.user_vs_balance

    def get_total_owe(self):
        return self.total_you_owe

    def set_total_owe(self, total_owe):
        self.total_you_owe = total_owe
        
    def get_total_payment(self):
        return self.total_payment

    def set_total_payment(self, total_payment):
        self.total_payment = total_payment

    def get_total_expense(self):
        return self.total_your_expense

    def set_total_expense(self, total_expense):
        self.total_your_expense = total_expense
    
    def get_total_get_back(self):
        return self.total_you_get_back
    
    def set_total_get_back(self, total_get_back):
        self.total_you_get_back = total_get_back

