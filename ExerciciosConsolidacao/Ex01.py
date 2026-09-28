products = ["Caderno", "Caneta", "Borracha"]
prices = [2.50, 0.80, 0.60]

inventory = dict(zip(products, prices))

total = sum(inventory.values())

print(inventory)
print("Total:", total)