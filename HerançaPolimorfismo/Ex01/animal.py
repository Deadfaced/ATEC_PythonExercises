class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def describe(self) -> str:
        return f"{self.name} é um animal"