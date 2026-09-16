def CheckPayments():
    """
    Receives payments inserted by the user and checks their status
    """

    payment_code: str
    refused_payments: str = ""

    while True:
        payment_code = input("Insira o código do pagamento: ")

        if payment_code == "fim":
            break
        elif payment_code.endswith("PAGO") or payment_code.endswith("PENDENTE"):
            pass
        elif payment_code.endswith("RECUSADO"):
            refused_payments += f"\n{payment_code}"

    print(f"Pagamentos recusados:{refused_payments}")



CheckPayments()