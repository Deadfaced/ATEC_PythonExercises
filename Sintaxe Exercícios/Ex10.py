def CheckPromoCode():
    """
    Gets a promo code from user and checks if it's valid
    """

    promo_code: str = input("Insira o código promocional: ")

    promo_code = promo_code.strip().lower()

    if promo_code[::-1] == promo_code:
        print("Código Promocional Especial Validado")
    else:
        print("Código inválido")

CheckPromoCode()