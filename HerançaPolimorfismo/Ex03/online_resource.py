import re

from resource import Resource


class OnlineResource(Resource):
    def __init__(self, title: str, url: str) -> None:
        super().__init__(title)
        self.url = url

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        if re.fullmatch(r"https?://\S+", value) is None:
            raise ValueError(f"URL inválido: {value}")
        self.__url = value
