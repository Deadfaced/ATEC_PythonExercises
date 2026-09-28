import re

text = """Texto introdutório.
[INICIO_REVISAO]
Rever secção 3.
Confirmar valores da tabela.
[FIM_REVISAO]
Texto final."""

padrao = r"""
    \[INICIO_REVISAO\]
    .*?
    \[FIM_REVISAO\]
"""

resultado = re.search(
    padrao,
    text,
    flags=re.DOTALL | re.VERBOSE
)

if resultado:
    bloco = resultado.group()
    print(repr(bloco))
else:
    print("Bloco de revisão não encontrado.")