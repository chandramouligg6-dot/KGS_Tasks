from abc import ABC, abstractmethod


# ---------- Abstract Parent ----------
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


# ---------- Child 1 ----------
class EmailNotification(Notification):
    def send(self, message):
        print(f'Email → Sending email: "{message}"')


# ---------- Child 2 ----------
class SMSNotification(Notification):
    def send(self, message):
        print(f'SMS → Sending SMS: "{message}"')


# ---------- Child 3 ----------
class WhatsAppNotification(Notification):
    def send(self, message):
        print(f'WhatsApp → Sending WhatsApp message: "{message}"')


# ---------- Test ----------
message = "Your order is confirmed"

for notifier in [EmailNotification(), SMSNotification(), WhatsAppNotification()]:
    notifier.send(message)