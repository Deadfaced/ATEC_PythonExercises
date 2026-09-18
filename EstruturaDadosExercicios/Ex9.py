def ValidateInvoices():
    """
    Checks if invoice is already saved in erp
    """

    local_erp_invoices: list[str] = [
        "INV-0000",
        "INV-0001",
        "INV-0002",
        "INV-0003",
        "INV-0004",
        "INV-0005",
        "INV-0001",
        "INV-0002",
        "INV-0003",
    ]
    portal_invoices: list[str] = [
        "INV-0000",
        "INV-0003",
        "INV-0006",
        "INV-0007",
        "INV-0008",
        "INV-0009",
    ]

    unique_local_erp_invoices = set(local_erp_invoices)
    unique_portal_invoices = set(portal_invoices)

    synced_invoices = unique_local_erp_invoices.intersection(unique_portal_invoices)
    portal_missing_invoices = unique_local_erp_invoices.difference(unique_portal_invoices)
    local_erp_missing_invoices = unique_portal_invoices.difference(unique_local_erp_invoices)

    print("Faturas em dias: ", synced_invoices)
    print("Faturas em falta no portal: ", portal_missing_invoices)
    print("Faturas não registadas localmente: ", local_erp_missing_invoices)

    invoice_warnings = [
        f"ACTION REQUIRED: Submeter fatura {invoice_id}"
        for invoice_id in portal_missing_invoices
    ]

    print(invoice_warnings)

ValidateInvoices()