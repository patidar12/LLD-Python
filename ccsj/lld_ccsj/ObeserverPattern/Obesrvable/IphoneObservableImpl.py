from typing import Set

from Obeserver.NotificationAlertObesrver import NotificationAlertObesrver
from .StocksObervable import StocksObervable

class IphoneStocksObervable(StocksObervable):

    def __init__(self):
        self.obervers: Set[NotificationAlertObesrver] = set()
        self.stock_count: int = 0
    
    def add(self, obesrver: NotificationAlertObesrver):
        self.obervers.add(obesrver)
    
    def remove(self, obesrver: NotificationAlertObesrver):
        self.obervers.remove(obesrver)
    
    def notifySubscriber(self):
        for obesrver in self.obervers:
            obesrver.update(self)

    def setStockCount(self, new_stock: int):
        if self.stock_count == 0 and new_stock > 0:
            self.notifySubscriber()
        self.stock_count += new_stock

    def getStockCount(self) -> int:
        return self.stock_count


