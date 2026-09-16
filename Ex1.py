def ApprovalIndex():
    """
    Asks the user for its approval index
    """
    CSAT: float = float(input("Insira o CSAT: "))

    # if CSAT in (0.0, 10.1):
    if CSAT >= 0.0 and CSAT <= 10.0:
        if CSAT >= 0.0 and CSAT < 4:
            print("Insuficiente")
        elif CSAT >= 4 and CSAT < 7:
            print("Suficiente")
        elif CSAT >= 7 and CSAT < 9:
            print("Bom")
        else:
            print("Excelente")
    else:
        print("Número inválido!")

ApprovalIndex()