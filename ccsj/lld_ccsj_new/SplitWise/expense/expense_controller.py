from typing import List

from expense import Expense
from expense.expense_split_type import ExpenseSplitType
from user import User
from expense.split import Split
from expense.split_factory import SplitFactory
from expense.split import ExpenseSplit
from balance_sheet_controller import BalaceSheetController

class ExpenseController:
    def __init__(self):
        # blance sheet controller required here,
        # becaus expenses is related to user
        # and we need to manage expenses in user object
        # so we required balancesheet object so we can update the users balancesheet here.
        self.balance_sheet_controller: BalaceSheetController = BalaceSheetController()
    
    def create_expense(
            self,
            eid: str,
            description: str,
            amount: float,
            split_type: ExpenseSplitType,
            paid_by: User,
            split_details: List[Split]
    ):
        split_object: ExpenseSplit = SplitFactory.get_split_object(split_type)
        split_object.validate_split_request(split_details, amount)
        expense = Expense(eid, description, amount, split_type, paid_by, split_details)
        self.balance_sheet_controller.update_iser_expense_balance_sheet(paid_by, split_details, amount)
        return expense
