from employee import Employee
from manager import Manager


def main() -> None:
    employee = Employee("Rui Costa")
    manager = Manager("Ana Silva", 5)

    print(employee.describe())
    print(manager.describe())

    try:
        print(manager.describe_wrong())
    except AttributeError as error:
        # O Python transforma __name em _Employee__name na classe Employee.
        # Em Manager, self.__name procura _Manager__name, que não existe.
        # Para corrigir, usar self.name, a property pública herdada de Employee.
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
