import re

texto = """Cabecalho
[INICIO_INCIDENTE]
Equipamento: Motor A
Falha: temperatura elevada
Nota: intervencao necessaria
[FIM_INCIDENTE]
Texto intermedio
[INICIO_INCIDENTE]
Equipamento: Sensor B
FALHA: sem resposta
Falha: ligacao interrompida
[FIM_INCIDENTE]
[INICIO_INCIDENTE]
Falha: bloco incompleto"""

padrao_bloco = re.compile(
    r"""
    \[INICIO_INCIDENTE\]
    .*?
    \[FIM_INCIDENTE\]
    """,
    flags=re.DOTALL | re.VERBOSE
)

padrao_falha = re.compile(
    r"^Falha:.*$",
    flags=re.MULTILINE | re.IGNORECASE
)

for numero, resultado in enumerate(
    padrao_bloco.finditer(texto),
    start=1
):
    bloco = resultado.group()
    inicio, fim = resultado.span()
    falhas = padrao_falha.findall(bloco)

    print(f"Bloco {numero}")
    print(f"Posição: [{inicio}, {fim}]")
    print("Linhas de falha:")

    for falha in falhas:
        print("-", falha)

    print()