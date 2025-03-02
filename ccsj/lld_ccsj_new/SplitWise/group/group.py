from typing import List
from expense.expense import Expense
from expense.expense_controller import ExpenseController

from user import User

class Group:
    def __init__(self):
        self.gid = None
        self.name = None
        self.group_memebers: List[User] = []
        self.expense_list: List[Expense] = []
        self.expense_controller: ExpenseController = ExpenseController()
    
    def add_member(self, member: User):
        self.group_memebers.append(member)
    
    def get_group_id(self):
        return self.gid
    
    def set_group_id(self, g)
    

    

