def CheckStatusCode():
    """
    Checks if the status code is valid
    """

    status_code: int = int(input("Insira o status code: "))

    while status_code < 0 or status_code >= 600:
        status_code = int(input("Insira o status code: "))

    match status_code:
        case 200:
            print(f"Código inserido {status_code}")
        case 200:
            print(f"Código inserido {status_code}")
        case 200:
            print(f"Código inserido {status_code}")
        case 200:
            print(f"Código inserido {status_code}")
        case _:
            print("Código de estado não documentado")

CheckStatusCode()