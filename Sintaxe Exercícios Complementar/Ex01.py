has_uppercase: bool = False
has_lowercase: bool = False
has_symbol: bool = False
has_number: bool = False
password: str = ""
password_length: int = 0

def ResetValues():
    global has_uppercase, has_lowercase, has_symbol, has_number, password, password_length

    has_number = False
    has_symbol = False
    has_lowercase = False
    has_uppercase = False
    password = ""
    password_length = 0

def PasswordValidation():
    """
    Receives a password from user input and checks if it's valid
    """
    global has_uppercase, has_lowercase, has_symbol, has_number, password, password_length

    while True:
        ResetValues()
        password = input("Insira a sua password: ")

        for char in password:
            if char.isupper():
                has_uppercase = True
            if char.islower():
                has_lowercase = True
            if char.isdigit():
                has_number = True
            match char:
                case "!" | "@" | "#" | "$" | "%" | "&":
                    has_symbol = True
            password_length += 1

        if has_symbol and has_number and has_lowercase and has_uppercase and password_length >= 12:
            print("Password inserida com sucesso!")
            break
        else:
            print("Password inválida, tente novamente!")
            if not has_uppercase:
                print("- Password não contém letra maiúscula")
            if not has_lowercase:
                print("- Password não contém letra minúscula")
            if not has_symbol:
                print("- Password não contém símbolos especiais")
            if not has_number:
                print("- Password não contém nenhum número")
            if password_length < 12:
                print("- Password contém menos de 12 dígitos")


PasswordValidation()