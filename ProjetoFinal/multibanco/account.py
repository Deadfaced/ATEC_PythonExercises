import messages
from movement import Movement
from validators import (
    validate_account_number,
    validate_amount,
    validate_iban,
    validate_name,
    validate_pin,
)


class Account:
    """Classe base: características comuns a todas as contas bancárias."""

    MAX_PIN_ATTEMPTS = 3
    WITHDRAWAL_MULTIPLE = 10

    def __init__(self, number: str, holder: str, pin: str, iban: str, initial_balance: float = 0.0) -> None:
        """
        Valida os dados e inicializa a conta.

        Args:
            number (str): Número da conta, com 4 dígitos.
            holder (str): Nome do titular (nome e apelido).
            pin (str): PIN com 4 dígitos.
            iban (str): IBAN português (PT50 seguido de 21 dígitos).
            initial_balance (float): Saldo inicial. Por defeito, 0.

        Raises:
            ValueError: Se algum dos dados for inválido, pela ordem: número
                (INVALID_ACCOUNT_NUMBER), titular (INVALID_HOLDER), PIN
                (INVALID_PIN), IBAN (INVALID_IBAN) e saldo inicial
                (INVALID_INITIAL_BALANCE).
        """
        # TODO: implementar
        raise NotImplementedError

    @property
    def number(self) -> str:
        """Devolve o número da conta."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def holder(self) -> str:
        """Devolve o nome do titular."""
        # TODO: implementar
        raise NotImplementedError

    @holder.setter
    def holder(self, value: str) -> None:
        """
        Valida e guarda o nome do titular.

        Args:
            value (str): Nome do titular.

        Raises:
            ValueError: Se o nome não tiver nome e apelido, só com letras
                (INVALID_HOLDER).
        """
        # TODO: implementar
        raise NotImplementedError

    @property
    def iban(self) -> str:
        """Devolve o IBAN da conta."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def balance(self) -> float:
        """Devolve o saldo atual (só de leitura)."""
        # TODO: implementar
        raise NotImplementedError

    @property
    def is_blocked(self) -> bool:
        """Indica se a conta está bloqueada."""
        # TODO: implementar
        raise NotImplementedError

    def account_type(self) -> str:
        """
        Devolve a designação do tipo de conta.

        Returns:
            str: messages.ACCOUNT_TYPE_BASE ('Conta'). As classes derivadas
                redefinem este método com a sua própria designação.
        """
        # TODO: implementar
        raise NotImplementedError

    def check_pin(self, pin: str) -> bool:
        """
        Verifica o PIN e bloqueia a conta após 3 tentativas falhadas seguidas.

        Um PIN correto repõe a zero o contador de tentativas falhadas.

        Args:
            pin (str): PIN introduzido.

        Returns:
            bool: True se o PIN estiver correto, False caso contrário.

        Raises:
            RuntimeError: Se a conta estiver bloqueada (ACCOUNT_BLOCKED).
        """
        # TODO: implementar
        raise NotImplementedError

    def unblock(self) -> None:
        """Desbloqueia a conta e repõe o contador de tentativas."""
        # TODO: implementar
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        """
        Deposita um valor na conta.

        Regista um movimento MOVEMENT_DEPOSIT com a descrição
        MOVEMENT_DEPOSIT_DESCRIPTION.

        Args:
            amount (float): Valor a depositar.

        Raises:
            ValueError: Se o valor for inválido (INVALID_AMOUNT).
        """
        # TODO: implementar
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        """
        Levanta um valor da conta.

        Regista um movimento MOVEMENT_WITHDRAWAL com a descrição
        MOVEMENT_WITHDRAWAL_DESCRIPTION.

        Args:
            amount (float): Valor a levantar, múltiplo de 10.

        Raises:
            ValueError: Se o valor for inválido (INVALID_AMOUNT), não for múltiplo
                de 10 (INVALID_WITHDRAWAL_MULTIPLE) ou ultrapassar os fundos
                disponíveis (INSUFFICIENT_FUNDS).
        """
        # TODO: implementar
        raise NotImplementedError

    def transfer_out(self, amount: float, destination_iban: str) -> None:
        """
        Regista a saída de uma transferência.

        Regista um movimento MOVEMENT_TRANSFER_OUT com a descrição
        'Para <IBAN de destino>'.

        Args:
            amount (float): Valor a transferir.
            destination_iban (str): IBAN da conta de destino.

        Raises:
            ValueError: Se o valor for inválido (INVALID_AMOUNT) ou ultrapassar
                os fundos disponíveis (INSUFFICIENT_FUNDS).
        """
        # TODO: implementar
        raise NotImplementedError

    def transfer_in(self, amount: float, origin_iban: str) -> None:
        """
        Regista a entrada de uma transferência.

        Regista um movimento MOVEMENT_TRANSFER_IN com a descrição
        'De <IBAN de origem>'.

        Args:
            amount (float): Valor recebido.
            origin_iban (str): IBAN da conta de origem.

        Raises:
            ValueError: Se o valor for inválido (INVALID_AMOUNT).
        """
        # TODO: implementar
        raise NotImplementedError

    def get_last_movements(self, count: int = 10) -> list[Movement]:
        """
        Devolve os movimentos mais recentes, do mais recente para o mais antigo.

        Args:
            count (int): Número máximo de movimentos. Por defeito, 10.

        Returns:
            list[Movement]: Lista com os movimentos mais recentes.
        """
        # TODO: implementar
        raise NotImplementedError

    def _available_funds(self) -> float:
        """
        Devolve o valor máximo que pode sair da conta.

        Returns:
            float: Na conta base, é o próprio saldo.
        """
        # TODO: implementar
        raise NotImplementedError

    def _validate_amount(self, amount: float) -> None:
        """
        Valida um valor monetário.

        Args:
            amount (float): Valor a validar.

        Raises:
            ValueError: Se o valor não for positivo ou tiver mais de 2 casas
                decimais (INVALID_AMOUNT).
        """
        # TODO: implementar
        raise NotImplementedError

    def _validate_withdrawal(self, amount: float) -> None:
        """
        Valida o valor de um levantamento, sem verificar os fundos.

        Args:
            amount (float): Valor a validar.

        Raises:
            ValueError: Se o valor for inválido (INVALID_AMOUNT) ou não for
                múltiplo de 10 (INVALID_WITHDRAWAL_MULTIPLE).
        """
        # TODO: implementar
        raise NotImplementedError

    def _credit(self, amount: float, movement_type: str, description: str) -> None:
        """
        Soma um valor ao saldo e regista o movimento.

        Args:
            amount (float): Valor a creditar.
            movement_type (str): Tipo de movimento.
            description (str): Descrição do movimento.
        """
        # TODO: implementar
        raise NotImplementedError

    def _debit(self, amount: float, movement_type: str, description: str) -> None:
        """
        Subtrai um valor ao saldo e regista o movimento.

        Args:
            amount (float): Valor a debitar.
            movement_type (str): Tipo de movimento.
            description (str): Descrição do movimento.
        """
        # TODO: implementar
        raise NotImplementedError

    def __register_movement(self, movement_type: str, amount: float, description: str) -> None:
        """
        Cria um movimento com o número seguinte e guarda-o na lista.

        Args:
            movement_type (str): Tipo de movimento.
            amount (float): Valor, negativo nos débitos.
            description (str): Descrição do movimento.
        """
        # TODO: implementar
        raise NotImplementedError

    def __str__(self) -> str:
        """
        Texto para o utilizador, usado na listagem de contas.

        Exemplos:
            1001 | Conta à ordem | João Silva | 1130.75 €
            1004 | Conta poupança | Ana Lopes | 0.00 € | BLOQUEADA
        """
        # TODO: implementar
        raise NotImplementedError

    def __repr__(self) -> str:
        """
        Texto técnico, com o nome da classe real do objeto.

        Exemplo:
            CheckingAccount('1001', 'João Silva', 1130.75)
        """
        # TODO: implementar
        raise NotImplementedError
