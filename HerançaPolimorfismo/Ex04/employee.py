class Employee:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def describe(self) -> str:
        return f"Funcionário: {self.name}"
