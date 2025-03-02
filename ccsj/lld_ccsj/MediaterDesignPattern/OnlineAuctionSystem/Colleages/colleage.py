from abc import ABC, abstractmethod


class Colleage(ABC):

    @abstractmethod
    def place_bid(self, bid_amount: float):
        pass

    @abstractmethod
    def receive_notification(self, bod_amount: float):
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
