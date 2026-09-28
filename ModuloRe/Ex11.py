import re

texto = """ENCOMENDA | 2026-000157 | ana.silva@exemplo.pt | 4470-123
Nota: pagamento pendente
encomenda | 2026-000158 | compras+web@empresa.pt | 1000-999
ENCOMENDA | 26-159 | email-invalido | 4000-001"""

padrao = re.compile(
    r"""
    ^encomenda
    [ \t]*\|[ \t]*
    (?P<referencia>\d{4}-\d{6})
    [ \t]*\|[ \t]*
    (?P<email>[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,})
    [ \t]*\|[ \t]*
    (?P<codigo_postal>\d{4}-\d{3})
    [ \t]*$
    """,
    flags=re.MULTILINE | re.IGNORECASE | re.VERBOSE
)

for resultado in padrao.finditer(texto):
    inicio, fim = resultado.span("referencia")

    print(resultado.group())
    print("Referência:", resultado.group("referencia"))
    print("Email:", resultado.group("email"))
    print("Código postal:", resultado.group("codigo_postal"))
    print(f"Posições da referência: [{inicio}, {fim}]")
    print()