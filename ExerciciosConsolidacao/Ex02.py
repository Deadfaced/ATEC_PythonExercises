import re

references = ["ABC1234", "AB123", "XYZ0007", "abc1234"]

pattern = r"^[A-Z]{3}\d{4}$"

for ref in references:
    if re.match(pattern, ref):
        print(ref, "-> válida")
    else:
        print(ref, "-> inválida")