import re

texto = (
    "Entrega em 4520-158, contacto 912345678, "
    "código antigo 4520158, morada 1000-999 Lisboa."
)

padrao = r"(?<!\d)\d{4}-\d{3}(?!\d)"

codigos_postais = re.findall(padrao, texto)

print(codigos_postais)