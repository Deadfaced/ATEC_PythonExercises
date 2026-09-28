import re

text = "Vendas do dia: 120.50€ em manhã, 89.90€ ao almoço e 340.00€ à tarde."

matches = re.findall(r"\d+\.\d{2}€", text)

values = []

for value in matches:
    values.append(float(value.replace("€", "")))

total = sum(values)

print(values)
print("Total:", total)