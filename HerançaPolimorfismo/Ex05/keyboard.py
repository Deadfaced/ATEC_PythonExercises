class Keyboard:
    def __init__(self, layout: str) -> None:
        self.layout = layout

    def type_text(self, text: str) -> str:
        return f"[{self.layout}] {text}"
