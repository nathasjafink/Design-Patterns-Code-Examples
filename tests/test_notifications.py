import unittest
from notifications.factory import NotificationFactory
from notifications.notification import EmailNotification, SMSNotification

class TestNotificationFactory(unittest.TestCase):
    def test_create_email_notification(self):
        notifier = NotificationFactory.create_notification("email")
        self.assertIsInstance(notifier, EmailNotification)

    def test_create_sms_notification(self):
        notifier = NotificationFactory.create_notification("sms")
        self.assertIsInstance(notifier, SMSNotification)

    def test_create_invalid_notification(self):
        with self.assertRaises(ValueError):
            NotificationFactory.create_notification("pigeon")

if __name__ == '__main__':
    unittest.main()
