orders = [1021, 1035, 1021, 1042, 1035, 1050]

unique_orders = []

for order in orders:
    if order not in unique_orders:
        unique_orders.append(order)

print(unique_orders)