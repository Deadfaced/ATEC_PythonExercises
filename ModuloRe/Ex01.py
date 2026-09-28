import re

mensagem = input("Introduza a mensagem: ")

padrao = r"^(Bom dia|Boa tarde|Boa noite)"

if re.match(padrao, mensagem, re.IGNORECASE):
    print("Saudação válida")
else:
    print("Saudação em falta")