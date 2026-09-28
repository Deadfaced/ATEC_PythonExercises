names = ["Ana", "Bruno", "Carla", "Diogo"]
departments = ["Vendas", "TI", "Vendas", "TI"]

employees_by_department = {}

for name, department in zip(names, departments):
    if department not in employees_by_department:
        employees_by_department[department] = []

    employees_by_department[department].append(name)

print(employees_by_department)