from typing import List
from Oberservable.StocksObservable import StocksObservable
from Obeserver.NotifyAlertObserver import NotifyAlertObeserver

class IPhoneObservable(StocksObservable):

    def __init__(self):
        self.observers: List[NotifyAlertObeserver] = []
        self.stock_count = 0
    
    def add(self, obesrver: NotifyAlertObeserver):
        self.observers.append(obesrver)

    def remove(self, obesrver: NotifyAlertObeserver):
        self.observers.remove(obesrver)

    def notify(self):
        for obesrver in self.observers:
            obesrver.update()

    def set_data(self, stocks: int):
        if self.stock_count == 0 and stocks != self.stock_count:
            self.notify()
        self.stock_count = stocks

    def get_data(self):
        return self.stock_count
