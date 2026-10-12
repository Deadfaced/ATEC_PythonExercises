import re
from typing import Optional


class Book:
    DEFAULT_GENRE = "Não classificado"

    def __init__(self, title: str, isbn: str, genre: Optional[str] = None) -> None:
        self.title = title
        self.isbn = isbn
        self.genre = self.DEFAULT_GENRE if genre is None else genre

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        # Valida apenas o formato, não o dígito de controlo do ISBN.
        if re.fullmatch(r"97[89][0-9]{10}", value) is None:
            raise ValueError(f"ISBN inválido: {value}")
        self.__isbn = value
