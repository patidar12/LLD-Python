

class Store:
    def notifier(self):
        from Obeserver.NotificationAlertObesrver import NotificationAlertObesrver
        from Obeserver.EmailAlertObesrver import EmailAlertObesrver
        from Obeserver.MobileAlertObesrver import MobileAlertObesrver
        from Obesrvable.StocksObervable import StocksObervable
        from Obesrvable.IphoneObservableImpl import IphoneStocksObervable
        iphone_stock_observable: StocksObervable = IphoneStocksObervable()
        email_obesrver: NotificationAlertObesrver = EmailAlertObesrver("xyz_email@gamil,com")
        email_obesrver2: NotificationAlertObesrver = EmailAlertObesrver("xyz2_email@gamil,com")
        mobile_obesrver: NotificationAlertObesrver = MobileAlertObesrver("xyz_mobile@gmail.com")
        iphone_stock_observable.add(email_obesrver)
        iphone_stock_observable.add(email_obesrver2)
        iphone_stock_observable.add(mobile_obesrver)
        iphone_stock_observable.setStockCount(10) # first time in stock will send the notification
        iphone_stock_observable.setStockCount(-10) # second time outofstock, not sending any notification
        iphone_stock_observable.setStockCount(2) # again instock, send notifications


Store().notifier()
