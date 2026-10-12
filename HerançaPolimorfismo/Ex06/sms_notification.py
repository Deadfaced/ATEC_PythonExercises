from notification import Notification


class SmsNotification(Notification):
    def send(self) -> str:
        return f"SMS enviado para {self.recipient}."
