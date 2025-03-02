from abc import ABC, abstractmethod
from Colleages.colleage import Colleage

class AuctionMediator(ABC):
    @abstractmethod
    def place_bid(self, bidder: Colleage, bid_amount: float):
        pass

    @abstractmethod
    def add_bidder(self, bidder: Colleage):
        pass
