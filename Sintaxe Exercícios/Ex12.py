def ChecksReadings():
    """
    Receives a list of readings and checks if maintenance is needed
    """

    consecutive_errors: int = 0
    readings: list[str] = [
        "OK",
        "FALHA",
        "OK",
        "FALHA",
        "FALHA",
        "FALHA"
    ]

    for current_reading in readings:
        match current_reading:
            case "FALHA":
                consecutive_errors += 1
                print(f"{current_reading}. Nº falhas: {consecutive_errors}")
            case "OK":
                consecutive_errors = 0
                print(f"{current_reading}")

        if consecutive_errors == 3:
            print("MANUTENÇÃO URGENTE NECESSÁRIA")
            break


ChecksReadings()