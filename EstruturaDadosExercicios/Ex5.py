def PurgeMultipleClients():
    """
    Takes a list of client id's and purge all repeated id's 
    """

    visitor_id_list: list[str] = [
        "5426",
        "6872",
        "1223",
        "9843",
        "1683",
        "6872",
        "9843",
        "5426",
        "1223",
        "1683"
    ]
    initial_id_qty: int = len(visitor_id_list)
    unique_ids = set(visitor_id_list)

    print(f"Número de cliques: {initial_id_qty}\nQuantidade de clientes únicos: {len(unique_ids)}\nIdentificadores repetidos: {unique_ids}")
    #for _ in unique_ids:
    #    print(_)


PurgeMultipleClients()