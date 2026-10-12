from task import Task


class TaskList:
    def __init__(self) -> None:
        # Cada objeto precisa da sua própria lista. Como atributo de classe,
        # a lista seria partilhada e as tarefas de diferentes objetos misturar-se-iam.
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def show_tasks(self) -> None:
        if not self.tasks:
            print("Não existem tarefas registadas.")
            return

        for number, task in enumerate(self.tasks, start=1):
            print(f"{number}. {task.title} (prioridade {task.priority})")
