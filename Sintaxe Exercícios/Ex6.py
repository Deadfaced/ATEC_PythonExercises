def CalculateSales():
    """
    Calculates the total amount of sales
    """

    sales_input: float
    total_sales: float = 0

    for sales in range(0, 5):
        sales_input = int(input(f"Insira o valor da {sales + 1}ª venda: "))
        if sales_input <= 0:
            print("Valor inválido!")
        else:
            total_sales += sales_input

    print(f"Valor total das vendas: {total_sales}")
    print(f"Média: {total_sales / 5}")

CalculateSales()