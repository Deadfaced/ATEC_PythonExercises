class Reservation:
    MAX_PEOPLE = 12

    def __init__(self, customer_name: str, people: int) -> None:
        if not customer_name.strip():
            raise ValueError("O nome do cliente é obrigatório.")
        if not 1 <= people <= self.MAX_PEOPLE:
            raise ValueError(f"Número de pessoas inválido: {people}")

        self.customer_name = customer_name
        self.people = people
