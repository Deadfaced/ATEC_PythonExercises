def CheckInvalidCharacters():
    """
    Receives a comment from the user and checks how many invalid characters there are
    """

    user_comment: str = input("Insira aqui o seu comentário: ")
    number_of_invalid_characters: int = 0

    for char in user_comment:
        match char:
            case '"' | "=" | "." | ",":
                number_of_invalid_characters += 1

    if number_of_invalid_characters > 0:
        print(f"Foram inseridos {number_of_invalid_characters} caracteres inválidos!")
    else:
        print("Comentário inserido com sucesso!")

CheckInvalidCharacters()