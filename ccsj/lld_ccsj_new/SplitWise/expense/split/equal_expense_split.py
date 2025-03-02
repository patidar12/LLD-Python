from typing import List

from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split

class EqualExpenseSplit(ExpenseSplit):

    def validate_split_request(self, split_details: List[Split], total_amount: float):
        # validate total amount in splits of each user is equal and overall equals to totalAmount or not
        amount_for_each_split = total_amount/len(split_details)
        total_split_amount = 0
        for split in split_details:
            if split.get_amount_owe() != amount_for_each_split:
                raise Exception("Amount equally not ditributes across splits...")
            total_split_amount += split.get_amount_owe()
        if total_split_amount != total_amount:
            raise Exception("total amount is not equal to split amounts...")
