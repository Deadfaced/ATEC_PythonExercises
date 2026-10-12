import sys

from task import Task
from task_list import TaskList


def main() -> None:
    task_list = TaskList()

    while True:
        print("1. Registar nova tarefa")
        print("2. Listar tarefas")
        print("3. Sair")
        option = input("Opção: ").strip()

        if option == "1":
            title = input("Título: ")
            try:
                priority = int(input("Prioridade: "))
            except ValueError:
                print("Erro: a prioridade tem de ser um número inteiro.")
                continue

            try:
                task = Task(title, priority)
            except ValueError as error:
                print(f"Erro: {error}")
                continue

            task_list.add_task(task)
            print("Tarefa registada.")
        elif option == "2":
            task_list.show_tasks()
        elif option == "3":
            print("A encerrar.")
            sys.exit(0)
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
