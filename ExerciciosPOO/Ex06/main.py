import sys

from printer import Printer


def main() -> None:
    printer = Printer("Impressora do 2.º piso", 10)

    try:
        printer.print_document(4)
        printer.print_document(20)
    except RuntimeError as error:
        print(f"Erro: {error}")
        print(f"Impressora ocupada? {printer.is_busy}")
        sys.exit(1)


if __name__ == "__main__":
    main()
