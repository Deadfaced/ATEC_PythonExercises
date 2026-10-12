import re


def validate_invoice_reference(reference: str) -> bool:
    """
    Valida uma referência de fatura no formato FAT-AAAA-NNNNNN.

    Args:
        reference (str): Referência da fatura.

    Returns:
        bool: True se a referência for válida, False caso contrário.
    """
    return bool(re.fullmatch(r"FAT-\d{4}-\d{6}", reference))


def validate_discount(discount: int) -> bool:
    """
    Valida se o desconto está entre 0 e 100.

    Args:
        discount (int): Percentagem de desconto.

    Returns:
        bool: True se o desconto for válido, False caso contrário.
    """
    return 0 <= discount <= 100


def main():
    references = ["FAT-2024-000157", "FAT-24-157"]
    discounts = [15, 150]

    for reference in references:
        if validate_invoice_reference(reference):
            print(f"{reference} -> válida")
        else:
            print(f"{reference} -> inválida")

    for discount in discounts:
        if validate_discount(discount):
            print(f"Desconto {discount}% -> válido")
        else:
            print(f"Desconto {discount}% -> inválido")


if __name__ == "__main__":
    main()