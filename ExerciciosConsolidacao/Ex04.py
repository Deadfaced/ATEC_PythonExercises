import re

messages = [
    "A minha encomenda 1023 ainda não chegou",
    "Quando é enviada a minha compra?",
    "Referente ao pedido 4501, preciso de alterar a morada"
]

result = {}

for message in messages:
    match = re.search(r"\b\d{4}\b", message)

    if match:
        result[message] = match.group()
    else:
        result[message] = None

print(result)