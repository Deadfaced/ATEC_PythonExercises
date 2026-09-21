def ManageWarehouse():
    """
    
    """

    warehouse_stock = {
        "Armazem_Norte": {
            "SKU-100": 50,
            "SKU-200": 0,
            "SKU-300": 1
        },
        "Armazem_Sul": {
            "SKU-100": 3,
            "SKU-200": 20,
            "SKU-300": 10
        }
    }

    order_items = [
        ("SKU-100", 5),
        ("SKU-300", 2),
        ("SKU-400", 1)
    ]

    out_of_stock_alerts = set()

    for product_id, ordered_quantity in order_items:
        product_shipped = False

        for warehouse_name, products in warehouse_stock.items():
            available_stock = products.get(product_id, 0)

            if available_stock >= ordered_quantity:
                products[product_id] -= ordered_quantity

                product_shipped = True
                break

        if not product_shipped:
            out_of_stock_alerts.add(product_id)

    print("\nStock atualizado:")
    for warehouse_name, products in warehouse_stock.items():
        print(f"{warehouse_name}: {products}")

    print("\nAlertas de falta de stock:", out_of_stock_alerts)

ManageWarehouse()