def SearchProduct():
    """
    Gets a product id from user and searches the DB for that product
    """

    products_list = [
        {
            "id": "P1",
            "name": "Monitor",
            "stock": "50"
        },
        {
            "id": "P2",
            "name": "Rato",
            "stock": "100"
        },
        {
            "id": "P3",
            "name": "Portátil",
            "stock": "10"
        }
    ] # type: ignore

    search_id: str = input("Insira o código do produto que pretende procurar: ")
    for _ in products_list:
        if _["id"] == search_id:
            print(f"Produto encontrado!\nNome: {_["name"]}\nStock: {_["stock"]}")
            break

SearchProduct()