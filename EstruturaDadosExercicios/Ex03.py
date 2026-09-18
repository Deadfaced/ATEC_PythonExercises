def Authentication():
    """
    Validates user authentication
    """

    API_CREDENTIAL = ("app_finance", "Secr3t2026")
    client_id: str = ""
    client_secret: str = ""

    client_id = input("Insira as suas credenciais")
    client_secret = input()
    if API_CREDENTIAL[0] == client_id and API_CREDENTIAL[1] == client_secret:
        print("Autenticação bem sucedida!")
    else:
        print("Falha de autenticação!")


Authentication()