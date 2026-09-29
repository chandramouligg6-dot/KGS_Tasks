from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f'Email → Sending email: "{message}"')

class SMSNotification(Notification):
    def send(self, message):
        print(f'SMS → Sending SMS: "{message}"')

class WhatsAppNotification(Notification):
    def send(self, message):
        print(f'WhatsApp → Sending WhatsApp message: "{message}"')

message = "Your order is confirmed"

for notifier in [EmailNotification(), SMSNotification(), WhatsAppNotification()]:
    notifier.send(message)