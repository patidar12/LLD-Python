from abc import ABC, abstractmethod

class StocksObervable(ABC):
    
    @abstractmethod
    def add(self, obesrver):
        pass
    
    @abstractmethod
    def remove(self, obesrver):
        pass
    
    @abstractmethod
    def notifySubscriber(self):
        pass

    @abstractmethod
    def setStockCount(self, new_stock):
        pass

    @abstractmethod
    def getStockCount(self):
        pass

