import re

mensagens = [
    "Por favor envie a factura para ana.silva@clientedomestico.pt assim que possível.",
    "Ainda não recebi resposta ao meu pedido."
]

padrao = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

for mensagem in mensagens:
    resultado = re.search(padrao, mensagem)

    if resultado:
        print("Extracted Email:", resultado.group())
    else:
        print("No email found.")