def Authentication():
    """
    Validates user authentication
    """

    PASSWORD: str = "admin123"
    number_of_remaining_attempts: int = 3
    user_input: str = ""

    while number_of_remaining_attempts > 0 and user_input != PASSWORD:
        user_input = input("Insira a password: ")

        if user_input != PASSWORD:
            number_of_remaining_attempts -= 1
            if number_of_remaining_attempts == 0:
                print("ACESSO BLOQUEADO!")
            else:
                print(f"Password incorreta! Número de tentativas restantes: {number_of_remaining_attempts}")
        else:
            print("Acesso concedido")

Authentication()