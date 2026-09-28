import re

text = """Tarefa concluída: revisão do documento
Reunião agendada para amanhã
tarefa CONCLUÍDA: envio do relatório
Nota: aguardar resposta do cliente"""

padrao = r"^tarefa concluída:.*$"

tarefas_concluidas = re.findall(
    padrao,
    text,
    flags=re.MULTILINE | re.IGNORECASE
)

print(tarefas_concluidas)