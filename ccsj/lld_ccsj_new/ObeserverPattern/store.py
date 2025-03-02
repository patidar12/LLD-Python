from Obeserver.EmailAlertObesrver import EmailAlertObesrver
from Obeserver.MobileAlertObesrver import MobileAlertObesrver
from Oberservable.IPhoneObeservable import IPhoneObservable

class StoreManager:
    def notify_me(self):
        iphone_obj = IPhoneObservable()
        observer1 = EmailAlertObesrver("manoj@gmail.com", iphone_obj)
        observer2 = EmailAlertObesrver("sunil@gmail.com", iphone_obj)
        observer3 = MobileAlertObesrver("9134123456", iphone_obj)
        iphone_obj.add(observer1)
        iphone_obj.add(observer2)
        iphone_obj.add(observer3)
        iphone_obj.set_data(100)

StoreManager().notify_me()