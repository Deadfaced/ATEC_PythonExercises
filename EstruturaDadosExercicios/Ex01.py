def ManageInvoices():
    """
    Manages invoices inserted by the user
    """


    invoices_list: list[str] = []
    
    for invoice in range(3):
        invoices_list.append(input("Insira o código da fatura: "))

    for test_invoice in invoices_list:
        if test_invoice == "INV-0000":
            invoices_list.remove("INV-0000")

    print(f"Lista de faturas: \n{invoices_list}")

ManageInvoices()