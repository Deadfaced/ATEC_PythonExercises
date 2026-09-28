import re

tickets = [
    {
        "cliente": "Ana",
        "mensagem": "A minha encomenda 1023 no valor de 45.90€ ainda não chegou"
    },
    {
        "cliente": "Bruno",
        "mensagem": "Quando é enviada a minha compra?"
    }
]

result = {}

for ticket in tickets:
    client = ticket["cliente"]
    message = ticket["mensagem"]

    order_match = re.search(r"\b\d{4}\b", message)
    value_match = re.search(r"\d+\.\d{2}€", message)

    result[client] = {
        "encomenda": order_match.group() if order_match else None,
        "valor": value_match.group().replace("€", "") if value_match else None
    }

print(result)