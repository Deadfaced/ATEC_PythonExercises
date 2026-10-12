class Printer:
    def __init__(self, name: str, paper_sheets: int) -> None:
        self.name = name
        self.paper_sheets = paper_sheets
        self.is_busy = False

    def print_document(self, pages: int) -> None:
        self.is_busy = True
        try:
            print(f"A imprimir {pages} páginas em {self.name}...")
            if pages > self.paper_sheets:
                raise RuntimeError("Papel insuficiente na impressora.")

            self.paper_sheets -= pages
            print(f"Impressão concluída. Folhas restantes: {self.paper_sheets}")
        finally:
            self.is_busy = False
            print("Impressora libertada.")
