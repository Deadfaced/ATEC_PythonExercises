def ValidateWorkerIdNumber():
    """
    Validates if the worker's identifying number is valid
    """

    digit_sum: int = 0
    worker_identifier: str = input("Insira o identificador do trabalhador: ")

    while worker_identifier == "" or not worker_identifier.isdigit():
        worker_identifier = input("Insira o identificador do trabalhador: ")

    for digit in worker_identifier:
        if int(digit) % 2 == 0:
            digit_sum += int(digit)

    print(f"Soma dos dígitos: {digit_sum}")



ValidateWorkerIdNumber()