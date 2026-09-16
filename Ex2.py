def CheckLicenseInactivity():
    """
    Checks if user's license has been inactive for too long
    """

    license_type: str = ""
    DaysSinceLastActivity: int = 0

    # if LicenseType not in ["trial", "premium"]:
    while license_type != "trial" and license_type != "premium":
        license_type = input("Introduza o tipo de licença: ")

    DaysSinceLastActivity = int(input("Insira quantos dias a conta esteve inativa: "))
    if license_type == "trial" and DaysSinceLastActivity > 30 or license_type == "premium" and DaysSinceLastActivity > 90:
        print("Requer suspensão imediata")
    else:
        print("Conta ativa")

CheckLicenseInactivity()