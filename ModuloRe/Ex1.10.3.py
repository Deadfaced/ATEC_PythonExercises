import re

textos = [
    "912345678",
    "Contacto disponível: 912345678 após as 18h",
    "91-234-5678",
    "Tel: abcdefghi"
]

padrao = r"(?<!\d)9\d{8}(?!\d)"

for texto in textos:
    resultado = re.search(padrao, texto)

    if resultado:
        print(f"{texto} → aceite")
        print(f"Número encontrado: {resultado.group()}")
    else:
        print(f"{texto} → rejeitado")