import re

text = """[2024-01-10] Material de escritório - almofadas - 45.00€
[2024-01-12] Deslocação - Porto - 32.50€"""

pattern = re.compile(
    r"\[(\d{4}-\d{2}-\d{2})\]\s(.+?)\s-\s(\d+\.\d{2})€"
)

expenses = []

for date, description, value in pattern.findall(text):
    expenses.append({
        "data": date,
        "descricao": description,
        "valor": float(value)
    })

print(expenses)