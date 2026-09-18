def AnalyzeSales():
    """
    Tracks sales and iterates on repeated sales, otherwise creates a new one
    """

    sales_list: list[str] = [
        "PRD-A",
        "PRD-B",
        "PRD-A",
        "PRD-C",
        "PRD-A",
        "PRD-B",
        "PRD-D",
        "PRD-B",
        "PRD-B"
    ]

    sales_tracker = dict()

    for sale in sales_list:
        if sale not in sales_tracker:
            sales_tracker[sale] = 1
        else:
            sales_tracker[sale] += 1


    bestsellers = [
        product
        for product, sales_count in sales_tracker.items()
        if sales_count >= 3
    ]

    print("Contagem de vendas:", sales_tracker)
    print("Bestsellers:", bestsellers)
    
AnalyzeSales()