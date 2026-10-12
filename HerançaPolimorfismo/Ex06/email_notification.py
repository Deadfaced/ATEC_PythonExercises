from notification import Notification


class EmailNotification(Notification):
    def send(self) -> str:
        return f"Email enviado para {self.recipient}."
