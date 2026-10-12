from employee import Employee


class Manager(Employee):
    def __init__(self, name: str, team_size: int) -> None:
        super().__init__(name)
        self.team_size = team_size

    def describe(self) -> str:
        return f"{super().describe()} | Equipa: {self.team_size} pessoas"

    def describe_wrong(self) -> str:
        return f"Gestor: {self.__name}"
