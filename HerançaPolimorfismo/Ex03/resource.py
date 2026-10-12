class Resource:
    def __init__(self, title: str) -> None:
        self.title = title

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if not value.strip():
            raise ValueError("O título não pode estar vazio.")
        self.__title = value
