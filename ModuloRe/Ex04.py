import re

texto = "farinha,  ovos ,leite,   açúcar"

ingredientes = [
    ingrediente
    for ingrediente in re.split(r"\s*,\s*", texto.strip())
    if ingrediente
]

print(ingredientes)