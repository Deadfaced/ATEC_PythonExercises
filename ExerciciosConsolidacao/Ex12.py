import re

text = """[2024-03-01] Deslocações: 25.50€
[2024-03-02] Material: 120.00€
[2024-03-03] Deslocações: 40.00€
[2024-03-04] Material: 15.75€
[2024-03-05] Refeições: 12.30€"""

pattern = re.compile(r"""
    ^\[
    \d{4}-\d{2}-\d{2}
    \]\s
    ([A-Za-zÀ-ÿ]+)
    :\s
    (\d+\.\d{2})
    €$
""", re.VERBOSE)

result = {}

for line in text.splitlines():
    match = pattern.match(line)

    if match:
        category = match.group(1)
        value = float(match.group(2))

        if category not in result:
            result[category] = {
                "transacoes": 0,
                "total": 0
            }

        result[category]["transacoes"] += 1
        result[category]["total"] += value

print(result)