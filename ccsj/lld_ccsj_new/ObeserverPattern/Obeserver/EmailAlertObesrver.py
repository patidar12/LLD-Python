from Obeserver.NotifyAlertObserver import NotifyAlertObeserver
from Oberservable.StocksObservable import StocksObservable

class EmailAlertObesrver(NotifyAlertObeserver):
    def __init__(self, uname, observable: StocksObservable):
        self.uname = uname
        self.observable: StocksObservable = observable
    
    def update(self):
        self.send_email(f"Email sent to: {self.uname}, Enjoy")

    def send_email(self, msg):
        print(msg)
