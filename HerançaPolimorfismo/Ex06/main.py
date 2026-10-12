from email_notification import EmailNotification
from notification import Notification
from sms_notification import SmsNotification


def main() -> None:
    notifications = [
        EmailNotification("ana@exemplo.pt", 2),
        SmsNotification("912345678", 5),
        Notification("Equipa de suporte", 1),
    ]

    for notification in notifications:
        print(notification)
        print(notification.send())

    print(notifications)

    try:
        SmsNotification("912345678", 9)
    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
