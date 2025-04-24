# notification.py

class Notification:
    def notify(self):
        raise NotImplementedError("Subclasses must implement this method")

class EmailNotification(Notification):
    def notify(self):
        print("Sending email notification")

class SMSNotification(Notification):
    def notify(self):
        print("Sending SMS notification")