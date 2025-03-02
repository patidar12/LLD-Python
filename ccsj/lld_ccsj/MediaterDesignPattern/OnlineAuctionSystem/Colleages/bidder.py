from Mediaters.auction_mediator import AuctionMediator
from Colleages.colleage import Colleage

class Bidder(Colleage):
    def __init__(self, name: str, mediator: AuctionMediator):
        self.name: str = name
        self.auction_mediator: AuctionMediator = mediator
    

    def place_bid(self, bid_amount: float) -> None:
        print(f"{self.name} Placing the bid.. Amount: {bid_amount}")
        self.auction_mediator.place_bid(bidder=self, bid_amount=bid_amount)

    def receive_notification(self, bid_amount: float) -> None:
        print(f"New bid for amount: {bid_amount} is placed!")

    def get_name(self) -> str:
        return self.name
