import re

comment = (
    "O Produto (Edição Especial) chegou danificado. "
    "Já contactei o suporte sobre o produto (edição especial) duas vezes."
)

keyword = "produto (edição especial)"

# Tratar a palavra-chave como texto literal
pattern = re.escape(keyword)

# Encontrar todas as ocorrências ignorando maiúsculas/minúsculas
matches = list(re.finditer(pattern, comment, re.IGNORECASE))

positions = []

for match in matches:
    positions.append([match.start(), match.end()])

# Substituir cada ocorrência por asteriscos
censored_text = re.sub(
    pattern,
    "*" * len(keyword),
    comment,
    flags=re.IGNORECASE
)

result = {
    "ocorrencias": len(matches),
    "posicoes": positions,
    "texto_censurado": censored_text
}

print(result)