def parse_order_line(line: str) -> dict:
    parts = line.split(":")

    if len(parts) != 2:
        raise ValueError

    return {
        "referencia": parts[0],
        "estado": parts[1]
    }


def main():
    lines = [
        "ENC-1021:Enviada",
        "ENC-1035",
        "ENC-1042:Pendente",
        "ENC-1050:Enviada:Urgente",
        "ENC-1060:Entregue"
    ]

    processed = 0
    failed = 0

    for line in lines:
        try:
            result = parse_order_line(line)
            print(result)
            processed += 1

        except ValueError:
            print(f"Aviso: linha inválida '{line}'")
            failed += 1

    print(f"Processadas: {processed} | Falhadas: {failed}")


if __name__ == "__main__":
    main()