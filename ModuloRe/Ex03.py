import re

texto = "Este   relatório  tem   espaços   a mais."

resultado = re.sub(r" +", " ", texto)

print(resultado)