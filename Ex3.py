def CheckStatusCode():
    """
    Checks if the status code is valid
    """

    StatusCode: int

    while StatusCode < 0 or StatusCode >= 600:
        int(input("Insira o status code: "))

    match StatusCode:
        case 200:
            print(f"Código inserido {StatusCode}")
        case 200:
            print(f"Código inserido {StatusCode}")
        case 200:
            print(f"Código inserido {StatusCode}")
        case 200:
            print(f"Código inserido {StatusCode}")
        case _:
            print("Código de estado não documentado")
