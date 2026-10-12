def add_invoice(current_total: float, amount: float) -> float:
    """
    Adiciona o valor de uma fatura ao total atual.

    Args:
        current_total (float): Total faturado até ao momento.
        amount (float): Valor da nova fatura.

    Returns:
        float: Novo total faturado.
    """
    return current_total + amount


def main():
    invoice_total = 0.0

    # Evitar global facilita os testes e a reutilização da função,
    # porque esta depende apenas dos parâmetros recebidos e do valor retornado.
    invoice_total = add_invoice(invoice_total, 120.50)
    invoice_total = add_invoice(invoice_total, 89.50)
    invoice_total = add_invoice(invoice_total, 45.00)

    print(f"Total facturado: {invoice_total}")


if __name__ == "__main__":
    main()