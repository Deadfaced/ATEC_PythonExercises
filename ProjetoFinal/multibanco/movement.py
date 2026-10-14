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
        # TODO: implementar
        raise NotImplementedError

    @property
    def number(self) -> int:
        """Devolve o número sequencial do movimento."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def movement_type(self) -> str:
        """Devolve o tipo de movimento."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def amount(self) -> float:
        """Devolve o valor do movimento (negativo nos débitos)."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def description(self) -> str:
        """Devolve a descrição do movimento."""
        # TODO: implementar
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Texto para o utilizador, usado na lista de movimentos.

        Exemplos:
            #001 | Depósito | +200.00 € | Depósito em numerário
            #002 | Levantamento | -50.00 € | Levantamento ATM
        """
        # TODO: implementar
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Texto técnico, usado por repr() e dentro de listas.

        Exemplo:
            Movement(1, 'Depósito', 200.0, 'Depósito em numerário')
        """
        # TODO: implementar
        raise NotImplementedError
