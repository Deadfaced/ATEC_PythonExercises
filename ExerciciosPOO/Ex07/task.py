class Task:
    def __init__(self, title: str, priority: int) -> None:
        self.title = title
        self.priority = priority

    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, value: int) -> None:
        if not 1 <= value <= 10:
            raise ValueError("A prioridade tem de estar entre 1 e 10.")
        self.__priority = value
