import messages
from account import Account


class CheckingAccount(Account):
    """Conta à ordem: permite saldo negativo até ao limite de descoberto."""

    OVERDRAFT_LIMIT = 200.0

    def account_type(self) -> str:
        """
        Devolve a designação do tipo de conta.

        Returns:
            str: messages.ACCOUNT_TYPE_CHECKING ('Conta à ordem').
        """
        # TODO: implementar
        raise NotImplementedError

    def _available_funds(self) -> float:
        """
        Devolve o valor máximo que pode sair da conta.

        Returns:
            float: Saldo mais o limite de descoberto.
        """
        # TODO: implementar
        raise NotImplementedError
