from Obeserver.NotifyAlertObserver import NotifyAlertObeserver
from Oberservable.StocksObservable import StocksObservable

class MobileAlertObesrver(NotifyAlertObeserver):
    def __init__(self, uname, observable: StocksObservable):
        self.uname = uname
        self.observable: StocksObservable = observable
    
    def update(self):
        self.send_msg(f"Msg sent to: {self.uname}, Enjoy!")

    def send_msg(self, msg):
        print(msg)