import re

paragrafo = "O relatório foi revisto. O novo relatório está pronto."
palavra = "relatório"

padrao = re.escape(palavra)

for ocorrencia in re.finditer(padrao, paragrafo):
    inicio, fim = ocorrencia.span()
    print(f"Ocorrência em [{inicio}, {fim}]")