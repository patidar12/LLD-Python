from typing import List
from user import User
from expense.split import Split
from balance import Balance
from user_expense_balance_sheet import UserExpenseBalanceSheet

class BalaceSheetController:
    def update_iser_expense_balance_sheet(self, expense_paid_by: User, splits: List[Split], total_expense_amount: float):
        # update the total amount paid of the expense paid by user
        paid_by_user_expense_sheet = expense_paid_by.get_user_expense_balance_sheet()
        paid_by_user_expense_sheet.set_total_payment(paid_by_user_expense_sheet.get_total_payment() + total_expense_amount)
        for split in splits:
            user_owe: User = split.get_user()
            owe_user_expense_sheet = user_owe.get_user_expense_balance_sheet()
            owe_amount = split.get_amount_owe()
            if expense_paid_by.get_uid() == user_owe.get_uid():
                paid_by_user_expense_sheet.set_total_expense(paid_by_user_expense_sheet.get_total_expense() + owe_amount)
            else:
                # update the balance of paid user
                paid_by_user_expense_sheet.set_total_get_back(paid_by_user_expense_sheet.get_total_get_back() + owe_amount)
            
            user_owe_balance = None
            if user_owe.get_uid() in paid_by_user_expense_sheet.get_user_vs_balance():
                user_owe_balance = paid_by_user_expense_sheet.get_user_vs_balance().get(user_owe.get_uid())
            else:
                user_owe_balance = Balance()
                paid_by_user_expense_sheet.get_user_vs_balance()[user_owe.get_uid()] = user_owe_balance
            user_owe_balance.set_amount_get_back(user_owe_balance.get_amount_get_back() + owe_amount)


            # update the balance sheet of owe user
            owe_user_expense_sheet.set_total_owe(owe_user_expense_sheet.get_total_owe() + owe_amount);
            owe_user_expense_sheet.set_total_expense(owe_user_expense_sheet.get_total_expense() + owe_amount);

            user_paid_balance = None
            if expense_paid_by.get_uid() in owe_user_expense_sheet.get_user_vs_balance():
                user_paid_balance = owe_user_expense_sheet.get_user_vs_balance().get(expense_paid_by.get_uid())
            else:
                user_paid_balance = Balance()
                owe_user_expense_sheet.get_user_vs_balance()[expense_paid_by.get_uid()] = user_paid_balance
            user_paid_balance.set_amount_owe(user_paid_balance.get_amount_owe() + owe_amount)

    def show_balance_sheet_of_user(user: User):
        print("---------------------------------------")

        print("Balance sheet of user : ", user.get_uid())

        user_expense_balance_sheet: UserExpenseBalanceSheet =  user.get_user_expense_balance_sheet()

        print("TotalYourExpense: ", user_expense_balance_sheet.get_total_expense())
        print("TotalGetBack: ", user_expense_balance_sheet.get_total_get_back())
        print("TotalYourOwe: ", user_expense_balance_sheet.get_total_owe())
        print("TotalPaymnetMade: ", user_expense_balance_sheet.get_total_payment())
        for user_id, balance in user_expense_balance_sheet.get_user_vs_balance().items():
            print(f"userId: {user_id}  YouGetBack: {balance.get_amount_get_back()}  YouOwe: {balance.get_amount_owe()}")

        print("---------------------------------------")
