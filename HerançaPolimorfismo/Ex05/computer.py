from keyboard import Keyboard


class Computer:
    def __init__(self, brand: str, layout: str) -> None:
        self.brand = brand
        self.__keyboard = Keyboard(layout)

    def write(self, text: str) -> None:
        print(f"{self.brand}: {self.__keyboard.type_text(text)}")
