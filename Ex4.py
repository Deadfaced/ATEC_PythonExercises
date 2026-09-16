def CheckQuota():
    """
    Checks if user has reached the limit of ree quota
    """

    user_quota: int = int(input("Insira o volume de dados armazenados em GBs: "))

    if user_quota >= 0:
        if user_quota < 50:
            print("Dentro da quota gratuita")
        elif user_quota >= 50 and user_quota < 100:
            print("Aviso: Aproximação do limite contratado")
        else:
            print("Erro: Quota excedida - bloqueio de uploads")
    else:
        print("Quota inválida!")

CheckQuota()