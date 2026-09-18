def ManageTickets():
    """
    Ticket management system
    """

    tickets: list[str] = [
        "TCK-101",
        "TCK-102",
        "TCK-103"
    ]
    user_selected_option: str = ""

    while True:
        user_selected_option = input("Escreva a opção desejada:\nNovo\nProcessar\nSair\n")
        match user_selected_option.lower():
            case "novo":
                tickets.append(f"TCK-10"+ str(len(tickets) + 1))
            case "processar":
                if tickets != []:
                    tickets.pop(0)
            case "sair":
                break
            case _:
                continue

    print("Lista de tickets: ")
    for ticket in tickets:
        print(ticket)

ManageTickets()