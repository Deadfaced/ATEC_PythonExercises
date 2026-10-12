def filter_customer_orders(orders: list[str]) -> list[str]:
    return [
        order
        for order in orders
        if not order.startswith(("INT-", "TST-"))
    ]


def main():
    orders = ["ENC-1021", "INT-0001", "ENC-1035", "TST-0042", "ENC-1050"]

    filtered_orders = filter_customer_orders(orders)

    print("Original:", orders)
    print("Filtrada:", filtered_orders)


if __name__ == "__main__":
    main()