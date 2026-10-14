import sys

import messages
from account import Account
from bank import Bank
from checking_account import CheckingAccount
from data import load_initial_data
from savings_account import SavingsAccount
from validators import parse_amount

ADMIN_PIN = "9999"


def main() -> None:
    """
    Carrega os dados iniciais e apresenta o menu inicial.

    A organização deste ficheiro é da responsabilidade do formando. Recomenda-se
    dividir o programa em funções com uma única responsabilidade (por exemplo:
    ler um valor, autenticar o cliente, mostrar cada menu, executar a sessão de
    cliente, executar a sessão de administrador e criar uma conta), todas com
    type hints e docstring, seguindo os menus e a ordem dos pedidos indicados
    no enunciado.
    """
    bank = Bank("Banco ATEC")
    load_initial_data(bank)
    # TODO: implementar o menu inicial
    raise NotImplementedError


if __name__ == "__main__":
    main()
