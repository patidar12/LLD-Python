from user_expense_balance_sheet import UserExpenseBalanceSheet

class User:
    def __init__(self, uid: str, name: str):
        self.uid = uid
        self.name = name
        self.user_expense_balance_sheet = UserExpenseBalanceSheet()

    def get_user_expense_balance_sheet(self):
        return self.user_expense_balance_sheet
    
    def get_uid(self):
        return self.uid