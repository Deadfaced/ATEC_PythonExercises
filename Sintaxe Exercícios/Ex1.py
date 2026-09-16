def ApprovalIndex():
    """
    Asks the user for its approval index
    """
    csat: float = float(input("Insira o CSAT: "))

    # if CSAT in (0.0, 10.1):
    if csat >= 0.0 and csat <= 10.0:
        if csat >= 0.0 and csat < 4:
            print("Insuficiente")
        elif csat >= 4 and csat < 7:
            print("Suficiente")
        elif csat >= 7 and csat < 9:
            print("Bom")
        else:
            print("Excelente")
    else:
        print("Número inválido!")

ApprovalIndex()