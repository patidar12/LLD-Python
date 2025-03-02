from enum import Enum
class AccountType(Enum):
    SAVING: str = "saving"
    CURRENT: str = "current"

class TransactionType(Enum):
    WITHDRAW: str = "withdraw"
    CHECK_BALANCE: str = "check balance"
