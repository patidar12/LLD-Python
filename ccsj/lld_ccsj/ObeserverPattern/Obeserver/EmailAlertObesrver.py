from Obesrvable.StocksObervable import StocksObervable
from .NotificationAlertObesrver import NotificationAlertObesrver

class EmailAlertObesrver(NotificationAlertObesrver):

    def __init__(self, email_id: str):
        self.email_id: str = email_id

    def update(self, obervable: StocksObervable):
        self.send_email("Product is in stock: Enjoy")

    def send_email(self, msg):
        print(f"email sent to: "+ self.email_id)
