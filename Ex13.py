def AddProducts():
    """
    Lets the user add products to the inventory
    """

    add_keyword: str = input("Insira o nome do produto: ")
    keyword_length: int
    number_of_invalid_products: int = 0

    while add_keyword != "sair":
        if add_keyword == "":
            continue
        else:
            keyword_length = 0
            for char in add_keyword:
                keyword_length += 1

            if keyword_length < 8:
                number_of_invalid_products += 1

        add_keyword = input("Insira o nome do produto: ")

    print(f"Foram inseridos {number_of_invalid_products} produtos inválidos!")


AddProducts()