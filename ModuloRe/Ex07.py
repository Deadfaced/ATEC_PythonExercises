import re

codigos = ["EVT-2024-ABC", "EVT-99-XY", "EVT-2025-QWE"]

padrao = r"EVT-(\d{4})-([A-Z]{3})"

for codigo in codigos:
    resultado = re.fullmatch(padrao, codigo)

    if resultado:
        numero = resultado.group(1)
        letras = resultado.group(2)
        tudo = resultado.groups()

        print(
            f"{codigo} → número: {numero}, "
            f"letras: {letras}, tudo: {tudo}"
        )
    else:
        print(f"{codigo} → inválido")