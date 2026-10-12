class Movie:
    def __init__(self, title: str, year: int) -> None:
        self.title = title
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return f"Movie({self.title!r}, {self.year})"

    