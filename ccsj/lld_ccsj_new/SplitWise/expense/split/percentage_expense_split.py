from typing import List

from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split

class PercentageExpenseSplit(ExpenseSplit):

    def validate_split_request(self, split_details: List[Split], total_amount: float):
        pass
