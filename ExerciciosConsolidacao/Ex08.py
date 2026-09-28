import re

movements = [
    "ABC1234: 15 unidades",
    "XYZ0007: 8 unidades",
    "ABC1234: 5 unidades",
    "movimento inválido"
]

pattern = re.compile(r"^([A-Z]{3}\d{4}): (\d+) unidades$")

totals = {}

for movement in movements:
    match = pattern.match(movement)

    if match:
        code = match.group(1)
        quantity = int(match.group(2))

        if code in totals:
            totals[code] += quantity
        else:
            totals[code] = quantity

print(totals)