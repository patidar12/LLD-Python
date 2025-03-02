from abc import ABC, abstractmethod
from Obeserver.NotifyAlertObserver import NotifyAlertObeserver

class StocksObservable(ABC):
    
    @abstractmethod
    def add(self, obesrver: NotifyAlertObeserver):
        pass

    @abstractmethod
    def remove(self, obesrver: NotifyAlertObeserver):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def set_data(self, stocks: int):
        pass

    @abstractmethod
    def get_data(self):
        pass
