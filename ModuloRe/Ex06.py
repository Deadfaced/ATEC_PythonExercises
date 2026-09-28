import re

termo = "creme (edição limitada)"
catalogo = (
    "Disponível: creme (edição limitada) — "
    "100ml, sabonete artesanal, óleo corporal."
)

padrao = re.escape(termo)
resultado = re.search(padrao, catalogo)

if resultado:
    print("Produto encontrado:", resultado.group())
else:
    print("Produto não encontrado.")