class Movement:
    """Representa um movimento de uma conta bancária."""

    def __init__(self, number: int, movement_type: str, amount: float, description: str) -> None:
        """
        Inicializa o movimento.

        Args:
            number (int): Número sequencial do movimento na conta.
            movement_type (str): Tipo de movimento (por exemplo, 'Depósito').
            amount (float): Valor, positivo para créditos e negativo para débitos.
            description (str): Descrição do movimento.
        """
        self.__number = number
        self.__movement_type = movement_type
        self.__amount = amount
        self.__description = description

    @property
    def number(self) -> int:
        """Devolve o número sequencial do movimento."""
        return self.__number

    @property
    def movement_type(self) -> str:
        """Devolve o tipo de movimento."""
        return self.__movement_type

    @property
    def amount(self) -> float:
        """Devolve o valor do movimento (negativo nos débitos)."""
        return self.__amount

    @property
    def description(self) -> str:
        """Devolve a descrição do movimento."""
        return self.__description

    def __str__(self) -> str:
        """
        Texto para o utilizador, usado na lista de movimentos.

        Exemplos:
            #001 | Depósito | +200.00 € | Depósito em numerário
            #002 | Levantamento | -50.00 € | Levantamento ATM
        """
        return (
            f"#{self.number:03d} | {self.movement_type} | "
            f"{self.amount:+.2f} € | {self.description}"
        )

    def __repr__(self) -> str:
        """
        Texto técnico, usado por repr() e dentro de listas.

        Exemplo:
            Movement(1, 'Depósito', 200.0, 'Depósito em numerário')
        """
        return (
            f"Movement({self.number!r}, {self.movement_type!r}, "
            f"{self.amount!r}, {self.description!r})"
        )
