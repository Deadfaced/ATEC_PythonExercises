def CheckValidReference():
    """
    Checks if a product reference is invalid
    """

    invalid_refs: list[str] = ["PRD-2015", "PRD-2018"]
    product_ref: str = input("Insira a referência do produto: ")

    if product_ref in invalid_refs:
        print("Erro: Operação rejeitada. Produto descontinuado e sem suporte")

CheckValidReference()