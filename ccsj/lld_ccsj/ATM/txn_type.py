from enum import Enum

class TransactionType(Enum):
    WITHDRAW: str = "withdraw"
    CHECK_BALANCE: str = "check balance"
