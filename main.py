# main.py
import sys
from factory.notifications.factory import NotificationFactory


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <email|sms>")
        return

    method = sys.argv[1] # get "sms" or "email"
    try: 
        notifier = NotificationFactory.create_notification(method)
        notifier.notify()
    except ValueError as e: 
        print(e)
    

if __name__ == "__main__":
    main()