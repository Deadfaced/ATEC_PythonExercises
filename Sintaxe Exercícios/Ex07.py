def CheckBatchNumber():
    """
    Checks if the batch number is valid
    """

    for batch_number in range(1, 36):
        if batch_number % 3 == 0 and batch_number % 5 == 0:
            print(f"{batch_number} ALERTA: Falsificação Detetada no Lote")
        elif batch_number % 3 == 0:
            print(f"{batch_number} Lote Aprovado")
        elif batch_number % 5 == 0:
            print(f"{batch_number} Lote Rejeitado (Falha de Qualidade)")

CheckBatchNumber()