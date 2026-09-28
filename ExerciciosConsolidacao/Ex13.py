import re

text = """[2024-01-10] Compressor A: Substituição de filtro
Empilhadora 3 - 2023-11-02 - Revisão geral
Linha não estruturada sem formato reconhecível
[2024-02-15] Compressor A: Verificação de pressão
Empilhadora 3 - 2024-01-20 - Troca de bateria"""

pattern = re.compile(
    r"^\[(\d{4}-\d{2}-\d{2})\]\s(.+?):\s(.+)$"
    r"|^(.+?)\s-\s(\d{4}-\d{2}-\d{2})\s-\s(.+)$"
)

result = {}
ignored_lines = 0

for line in text.splitlines():
    match = pattern.match(line)

    if match:
        if match.group(1):
            # Formato recente
            date = match.group(1)
            equipment = match.group(2)
            description = match.group(3)
        else:
            # Formato antigo
            equipment = match.group(4)
            date = match.group(5)
            description = match.group(6)

        if equipment not in result:
            result[equipment] = []

        result[equipment].append({
            "data": date,
            "descricao": description
        })

    else:
        ignored_lines += 1

print(result)
print("Linhas ignoradas:", ignored_lines)