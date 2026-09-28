import re

report = """Vendedor: Ana | Valor: 120.50€
Vendedor: Bruno | Valor: 89.90€
Vendedor: Ana | Valor: 200.00€"""

pattern = re.compile(r"Vendedor: ([A-Za-zÀ-ÿ]+) \| Valor: (\d+\.\d{2})€")

result = {}

for seller, value in pattern.findall(report):
    value = float(value)

    if seller not in result:
        result[seller] = {
            "vendas": 0,
            "total": 0
        }

    result[seller]["vendas"] += 1
    result[seller]["total"] += value

print(result)