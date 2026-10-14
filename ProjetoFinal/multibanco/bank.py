import messages
from account import Account
from validators import validate_iban


class Bank:
    """Banco: tem um conjunto de contas, indexadas pelo número."""

    def __init__(self, name: str) -> None:
        """
        Inicializa o banco sem contas.

        Args:
            name (str): Nome do banco.
        """
        # TODO: implementar
        raise NotImplementedError

    def add_account(self, account: Account) -> None:
        """
        Acrescenta uma conta ao banco.

        Args:
            account (Account): Conta a acrescentar.

        Raises:
            ValueError: Se já existir uma conta com o mesmo número ou IBAN
                (mensagens com f-string, ver enunciado).
        """
        # TODO: implementar
        raise NotImplementedError

    def find_account(self, number: str) -> Account | None:
        """
        Procura uma conta pelo número.

        Args:
            number (str): Número da conta.

        Returns:
            Account | None: A conta encontrada, ou None.
        """
        # TODO: implementar
        raise NotImplementedError

    def find_by_iban(self, iban: str) -> Account | None:
        """
        Procura uma conta pelo IBAN.

        Args:
            iban (str): IBAN da conta.

        Returns:
            Account | None: A conta encontrada, ou None.
        """
        # TODO: implementar
        raise NotImplementedError

    def list_accounts(self) -> list[Account]:
        """
        Devolve todas as contas, ordenadas pelo número.

        Returns:
            list[Account]: Lista de contas.
        """
        # TODO: implementar
        raise NotImplementedError

    def next_account_number(self) -> str:
        """
        Calcula o número da próxima conta a criar.

        Returns:
            str: Número seguinte ao maior existente, com 4 dígitos, ou '1001'
                se o banco ainda não tiver contas.
        """
        # TODO: implementar
        raise NotImplementedError

    def generate_iban(self, number: str) -> str:
        """
        Gera o IBAN de uma conta a partir do seu número.

        Args:
            number (str): Número da conta.

        Returns:
            str: IBAN no formato PT50 seguido de 21 dígitos.
        """
        # TODO: implementar
        raise NotImplementedError

    def remove_account(self, number: str) -> None:
        """
        Elimina uma conta, desde que tenha saldo zero.

        Args:
            number (str): Número da conta.

        Raises:
            ValueError: Se a conta não existir (ACCOUNT_NOT_FOUND) ou o saldo
                não for zero (ACCOUNT_HAS_BALANCE).
        """
        # TODO: implementar
        raise NotImplementedError

    def unblock_account(self, number: str) -> None:
        """
        Desbloqueia uma conta.

        Args:
            number (str): Número da conta.

        Raises:
            ValueError: Se a conta não existir (ACCOUNT_NOT_FOUND) ou não estiver
                bloqueada (ACCOUNT_NOT_BLOCKED).
        """
        # TODO: implementar
        raise NotImplementedError

    def transfer(self, origin: Account, destination_iban: str, amount: float) -> None:
        """
        Transfere um valor entre duas contas do banco.

        A saída na origem é feita antes da entrada no destino: se a saída
        falhar, nenhuma das contas é alterada.

        Args:
            origin (Account): Conta de origem.
            destination_iban (str): IBAN da conta de destino.
            amount (float): Valor a transferir.

        Raises:
            ValueError: Pela ordem: IBAN com formato inválido (INVALID_IBAN),
                destino inexistente (DESTINATION_NOT_FOUND), destino igual à
                origem (SAME_ACCOUNT_TRANSFER) e, por fim, os erros de
                transfer_out (valor ou fundos).
        """
        # TODO: implementar
        raise NotImplementedError
