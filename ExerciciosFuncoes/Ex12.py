import sys


def load_invoice_lines(path: str) -> list[str]:
    """
    Lê as linhas de um ficheiro de faturas.

    Args:
        path (str): Caminho para o ficheiro.

    Returns:
        list[str]: Lista de linhas do ficheiro.
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def parse_invoice_line(line: str) -> dict:
    """
    Converte uma linha no formato REFERÊNCIA;VALOR num dicionário.

    Args:
        line (str): Linha da fatura.

    Returns:
        dict: Dicionário com a referência e o valor.

    Raises:
        ValueError: Se a linha não tiver o formato esperado.
    """
    parts = line.split(";")

    if len(parts) != 2:
        raise ValueError

    reference = parts[0]
    value = float(parts[1])

    return {
        "referencia": reference,
        "valor": value
    }


def calculate_totals(invoices: list[dict], vat_rate: int = 23) -> dict:
    """
    Calcula o total sem IVA, o valor do IVA e o total com IVA.

    Args:
        invoices (list[dict]): Lista de faturas.
        vat_rate (int): Taxa de IVA.

    Returns:
        dict: Totais calculados.
    """
    total_without_vat = sum(invoice["valor"] for invoice in invoices)
    vat = total_without_vat * vat_rate / 100
    total_with_vat = total_without_vat + vat

    return {
        "total_sem_iva": total_without_vat,
        "iva": vat,
        "total_com_iva": total_with_vat
    }


def main():
    invoices = []
    ignored = 0
    exit_code = 0

    try:
        path = sys.argv[1]
        lines = load_invoice_lines(path)

        for line in lines:
            try:
                invoice = parse_invoice_line(line)
                invoices.append(invoice)
            except ValueError:
                print(f"Aviso: linha inválida '{line}'")
                ignored += 1

        totals = calculate_totals(invoices)

        print(f"Facturas processadas: {len(invoices)} | Ignoradas: {ignored}")
        print(f"Total sem IVA: {totals['total_sem_iva']}")
        print(f"IVA (23%): {totals['iva']}")
        print(f"Total com IVA: {totals['total_com_iva']}")

    except FileNotFoundError:
        print(f"Erro: o ficheiro '{sys.argv[1]}' não foi encontrado.")
        exit_code = 1

    except PermissionError:
        print(f"Erro: sem permissão para ler o ficheiro '{sys.argv[1]}'.")
        exit_code = 1

    finally:
        print("Processamento terminado.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()