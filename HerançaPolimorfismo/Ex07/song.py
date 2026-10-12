class Song:
    def __init__(self, title: str) -> None:
        self.set_title(title)

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        if not title.strip():
            raise ValueError("O título da música não pode estar vazio.")
        self.__title = title

    def __repr__(self) -> str:
        return f"Song(title={self.get_title()!r})"
