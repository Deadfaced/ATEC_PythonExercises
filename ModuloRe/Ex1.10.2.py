import re

relatorio = """Falha: motor bloqueado
Info: revisão concluída
Falha: sensor sem resposta
Nota: peça substituída"""

padrao = r"^Falha:.*$"

resultados = re.findall(padrao, relatorio, re.MULTILINE)

for linha in resultados:
    print(linha)