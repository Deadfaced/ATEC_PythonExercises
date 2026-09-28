import re

texto = "FAT-2026-000157; REC-2025-000034, FAT-26-157 DOC-2026-000001"

referencias = re.split(r"[,;\s]+", texto.strip())

padrao = re.compile(r"(FAT|REC)-(\d{4})-(\d{6})")

for referencia in referencias:
    resultado = padrao.fullmatch(referencia)

    if resultado:
        tipo, ano, numero = resultado.groups()

        print(
            f"{referencia} → tipo: {tipo}, "
            f"ano: {ano}, numero: {numero}"
        )
    else:
        print(f"{referencia} → inválida")