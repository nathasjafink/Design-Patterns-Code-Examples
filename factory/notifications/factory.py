# factory.py

from .notification import EmailNotification, SMSNotification

class NotificationFactory:
    @staticmethod
    def create_notification(method):
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        else:
            raise ValueError(f"Unknown notification method: {method}")