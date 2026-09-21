def GetDepartmentById():
    """
    Receives a department id and returns the respective department if found
    """

    departments_list = {
            10: "Recursos humanos",
            20: "Financeiro",
            30: "Operações",
        }

    department_id: int = int(input("Insira o id do departamento: "))
    print(departments_list.get(department_id, "Departamento não encontrado!"))
    # if departments_list.get(department_id):
    #     print("Departamento encontrado: ", departments_list.get(department_id))
    # else:
    #     print("Departamento não encontrado!")

GetDepartmentById()