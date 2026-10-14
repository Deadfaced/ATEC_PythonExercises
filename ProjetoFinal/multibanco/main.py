import sys

import messages
from account import Account
from bank import Bank
from checking_account import CheckingAccount
from data import load_initial_data
from savings_account import SavingsAccount
from validators import parse_amount

ADMIN_PIN = "9999"



def read_amount() -> float:
    """Pede e converte um valor monetário."""
    return parse_amount(input("Valor: "))


def login(bank: Bank) -> Account | None:
    """Autentica o cliente, respeitando o bloqueio e as tentativas de PIN."""
    account = bank.find_account(input("Número da conta: "))
    if account is None:
        print(messages.ACCOUNT_NOT_FOUND)
        return None
    if account.is_blocked:
        print(messages.ACCOUNT_BLOCKED)
        return None
    while not account.is_blocked:
        if account.check_pin(input("PIN: ")):
            print(f"Bem-vindo(a), {account.holder}.")
            return account
        if account.is_blocked:
            print(messages.ACCOUNT_NOW_BLOCKED)
        else:
            print(messages.WRONG_PIN)
    return None


def client_session(bank: Bank, account: Account) -> None:
    """Apresenta o menu de cliente e executa as operações da conta."""
    while True:
        print("\n1. Consultar saldo\n2. Levantamento\n3. Depósito")
        print("4. Transferência\n5. Últimos 10 movimentos\n6. Terminar sessão")
        option = input("Opção: ")
        try:
            if option == "1":
                print(f"Saldo disponível: {account.balance:.2f} €")
            elif option == "2":
                account.withdraw(read_amount())
                print(f"Levantamento efetuado. Saldo: {account.balance:.2f} €")
            elif option == "3":
                account.deposit(read_amount())
                print(f"Depósito efetuado. Saldo: {account.balance:.2f} €")
            elif option == "4":
                destination_iban = input("IBAN de destino: ")
                amount = read_amount()
                bank.transfer(account, destination_iban, amount)
                print(f"Transferência efetuada. Saldo: {account.balance:.2f} €")
            elif option == "5":
                movements = account.get_last_movements()
                if not movements:
                    print(messages.NO_MOVEMENTS)
                for movement in movements:
                    print(movement)
            elif option == "6":
                print(messages.SESSION_ENDED)
                return
            else:
                print(messages.INVALID_OPTION)
        except ValueError as error:
            print(f"{messages.ERROR_PREFIX}{error}")


def create_account(bank: Bank) -> None:
    """Pede os dados, cria uma conta do tipo escolhido e adiciona-a ao banco."""
    account_type = input("Tipo de conta (1 - à ordem, 2 - poupança): ")
    if account_type not in ("1", "2"):
        raise ValueError(messages.INVALID_ACCOUNT_TYPE)
    holder = input("Nome do titular: ")
    pin = input("PIN: ")
    initial_balance = read_amount()
    number = bank.next_account_number()
    iban = bank.generate_iban(number)
    if account_type == "1":
        account = CheckingAccount(number, holder, pin, iban, initial_balance)
    else:
        account = SavingsAccount(number, holder, pin, iban, initial_balance)
    bank.add_account(account)
    print(f"Conta criada: {account}")
    print(f"IBAN: {account.iban}")


def admin_session(bank: Bank) -> None:
    """Apresenta o menu de administrador e trata os erros das operações."""
    while True:
        print("\n1. Criar conta\n2. Listar contas\n3. Eliminar conta")
        print("4. Desbloquear conta\n5. Terminar sessão")
        option = input("Opção: ")
        try:
            if option == "1":
                create_account(bank)
            elif option == "2":
                for account in bank.list_accounts():
                    print(account)
            elif option == "3":
                bank.remove_account(input("Número da conta: "))
                print(messages.ACCOUNT_REMOVED)
            elif option == "4":
                bank.unblock_account(input("Número da conta: "))
                print(messages.ACCOUNT_UNBLOCKED)
            elif option == "5":
                print(messages.SESSION_ENDED)
                return
            else:
                print(messages.INVALID_OPTION)
        except ValueError as error:
            print(f"{messages.ERROR_PREFIX}{error}")

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
    while True:
        print("\n=== Multibanco ===")
        print("1. Entrar como cliente\n2. Entrar como administrador\n3. Sair")
        option = input("Opção: ")
        if option == "1":
            account = login(bank)
            if account is not None:
                client_session(bank, account)
        elif option == "2":
            if input("PIN de administrador: ") == ADMIN_PIN:
                admin_session(bank)
            else:
                print(messages.WRONG_ADMIN_PIN)
        elif option == "3":
            print(messages.GOODBYE)
            return
        else:
            print(messages.INVALID_OPTION)


if __name__ == "__main__":
    main()
