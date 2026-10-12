def calculate_total(amount: float, vat_rate: int = 23) -> float:
    """
    Calcula o valor total com IVA.

    Args:
        amount (float): Valor sem IVA.
        vat_rate (int): Taxa de IVA em percentagem.

    Returns:
        float: Valor total com IVA.
    """
    return amount * (1 + vat_rate / 100)


def main():
    amount = 100.0

    print(f"Total com IVA (23%): {calculate_total(amount)}")
    print(f"Total com IVA (6%): {calculate_total(amount, 6)}")


if __name__ == "__main__":
    main()