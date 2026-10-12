import sys


def validate_arguments(args: list[str]) -> tuple[str, str]:
    if len(args) != 3:
        raise IndexError(
            "número de argumentos inválido. "
            "Uso: python report.py <CLIENTE> <PDF|CSV>"
        )

    client = args[1]
    report_format = args[2]

    if report_format not in ("PDF", "CSV"):
        raise ValueError(
            f"formato '{report_format}' inválido. Utilize PDF ou CSV."
        )

    return client, report_format


def main():
    exit_code = 0

    try:
        client, report_format = validate_arguments(sys.argv)
        print(f"A gerar relatório {report_format} para {client}")

    except IndexError as error:
        print(f"Erro: {error}")
        exit_code = 1

    except ValueError as error:
        print(f"Erro: {error}")
        exit_code = 1

    finally:
        print("Fim da execução.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()