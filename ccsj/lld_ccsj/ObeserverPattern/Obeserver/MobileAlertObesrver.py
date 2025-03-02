from Obesrvable.StocksObervable import StocksObervable
from .NotificationAlertObesrver import NotificationAlertObesrver

class MobileAlertObesrver(NotificationAlertObesrver):

    def __init__(self, email_id: str):
        self.user_name: str = email_id

    def update(self, obervable: StocksObervable):
        self.send_msg("Product is in stock: Enjoy")

    def send_msg(self, msg):
        print(f"msg sent to: "+ self.user_name)
