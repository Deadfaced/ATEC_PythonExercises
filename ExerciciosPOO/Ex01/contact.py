class Contact:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def show_details(self) -> None:
        print(f"{self.name}: {self.phone}")
