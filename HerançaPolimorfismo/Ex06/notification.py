class Notification:
    def __init__(self, recipient: str, priority: int) -> None:
        self.recipient = recipient
        self.priority = priority

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, value: int) -> None:
        if not 1 <= value <= 5:
            raise ValueError("A prioridade tem de estar entre 1 e 5.")
        self.__priority = value

    def send(self) -> str:
        return "Notificação genérica enviada."

    def __str__(self) -> str:
        return f"[Prioridade {self.priority}] Para: {self.recipient}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.recipient!r}, {self.priority})"
