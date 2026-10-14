"""
Teste automático dos cenários do trabalho "Simulação de um Multibanco".

Corre os 35 cenários do enunciado (secção 9) sobre a pasta multibanco e indica,
para cada um, se o resultado esperado aparece na saída do programa. É o mesmo
script usado na avaliação.

Utilização (na pasta onde está este ficheiro):
    python corrigir_cenarios.py multibanco

Notas:
    - Cada cenário arranca o main.py de novo, com os dados iniciais do data.py.
    - Um cenário só passa se as mensagens esperadas aparecerem pela ordem indicada
      e o programa terminar sem erros (código de saída 0).
    - Enquanto o main.py não tiver os menus, todos os cenários falham com
      NotImplementedError. É o esperado: até lá, teste as classes com um
      pequeno script próprio.
    - Para cada cenário que falha, o script indica a primeira mensagem em falta
      e, se o programa terminou com erro, a última linha desse erro.
    - Não altere este ficheiro.
"""

import os
import subprocess
import sys
from pathlib import Path

TIMEOUT_SECONDS = 10

# (número, descrição, respostas dadas ao programa, mensagens esperadas por ordem)
S = [
    (
        "T01", "Login com dados corretos",
        ["1", "1001", "1234", "6", "3"],
        ["Bem-vindo(a), João Silva."],
    ),
    (
        "T02", "Login com conta inexistente",
        ["1", "9999", "3"],
        ["Conta não encontrada."],
    ),
    (
        "T03", "PIN errado uma vez e depois correto",
        ["1", "1001", "0000", "1234", "6", "3"],
        ["PIN incorreto.", "Bem-vindo(a), João Silva."],
    ),
    (
        "T04", "Três PIN errados bloqueiam a conta",
        ["1", "1001", "0000", "1111", "2222", "1", "1001", "3"],
        [
            "PIN incorreto.",
            "PIN incorreto.",
            "PIN incorreto. A conta foi bloqueada.",
            "Conta bloqueada. Contacte o administrador.",
        ],
    ),
    (
        "T05", "Consultar saldo",
        ["1", "1001", "1234", "1", "6", "3"],
        ["Saldo disponível: 1130.75 €"],
    ),
    (
        "T06", "Levantamento válido",
        ["1", "1001", "1234", "2", "50", "6", "3"],
        ["Levantamento efetuado. Saldo: 1080.75 €"],
    ),
    (
        "T07", "Levantamento que não é múltiplo de 10",
        ["1", "1001", "1234", "2", "55", "6", "3"],
        ["Erro: O valor do levantamento tem de ser múltiplo de 10 €."],
    ),
    (
        "T08", "Letras no valor",
        ["1", "1001", "1234", "2", "abc", "6", "3"],
        ["Erro: Valor inválido. Introduza um número."],
    ),
    (
        "T09", "Conta à ordem: descoberto até 200 €",
        ["1", "1003", "5678", "2", "750", "2", "60", "1", "6", "3"],
        [
            "Levantamento efetuado. Saldo: -150.00 €",
            "Erro: Saldo insuficiente.",
            "Saldo disponível: -150.00 €",
        ],
    ),
    (
        "T10", "Depósito com vírgula decimal",
        ["1", "1001", "1234", "3", "25,50", "6", "3"],
        ["Depósito efetuado. Saldo: 1156.25 €"],
    ),
    (
        "T11", "Depósito com mais de 2 casas decimais",
        ["1", "1001", "1234", "3", "10.555", "6", "3"],
        ["Erro: O valor tem de ser positivo e ter no máximo 2 casas decimais."],
    ),
    (
        "T12", "Conta poupança: levantamento com comissão",
        ["1", "1002", "4321", "2", "100", "5", "6", "3"],
        [
            "Levantamento efetuado. Saldo: 2348.00 €",
            "#004 | Comissão | -1.00 € | Comissão de levantamento",
            "#003 | Levantamento | -100.00 € | Levantamento ATM",
        ],
    ),
    (
        "T13", "Conta poupança: saldo não cobre a comissão",
        ["1", "1002", "4321", "2", "2450", "1", "6", "3"],
        [
            "Erro: Saldo insuficiente para o levantamento e a comissão.",
            "Saldo disponível: 2449.00 €",
        ],
    ),
    (
        "T14", "Transferência entre contas",
        [
            "1", "1001", "1234", "4", "PT50000000000000000001003", "100", "6", "1", "1003",
            "5678", "1", "5", "6", "3",
        ],
        [
            "Transferência efetuada. Saldo: 1030.75 €",
            "Saldo disponível: 700.00 €",
            "#002 | Transferência recebida | +100.00 € | De PT50000000000000000001001",
        ],
    ),
    (
        "T15", "Transferência para IBAN inexistente",
        ["1", "1001", "1234", "4", "PT50000000000000000009999", "100", "6", "3"],
        ["Erro: IBAN de destino não encontrado."],
    ),
    (
        "T16", "Transferência para a própria conta",
        ["1", "1001", "1234", "4", "PT50000000000000000001001", "100", "6", "3"],
        ["Erro: Não é possível transferir para a própria conta."],
    ),
    (
        "T17", "Transferência sem saldo não altera nenhuma conta",
        [
            "1", "1002", "4321", "4", "PT50000000000000000001003", "5000", "1", "6", "1",
            "1003", "5678", "1", "6", "3",
        ],
        ["Erro: Saldo insuficiente.", "Saldo disponível: 2449.00 €", "Saldo disponível: 600.00 €"],
    ),
    (
        "T18", "Últimos 10 movimentos, do mais recente para o mais antigo",
        ["1", "1001", "1234", "5", "6", "3"],
        [
            "#011 | Levantamento | -30.00 € | Levantamento ATM",
            "#010 | Depósito | +60.00 € | Depósito em numerário",
            "#002 | Levantamento | -50.00 € | Levantamento ATM",
        ],
    ),
    (
        "T19", "Conta sem movimentos",
        [
            "2", "9999", "1", "2", "Ana Lopes", "1111", "50", "5", "1", "1004", "1111", "5",
            "6", "3",
        ],
        ["Ainda não existem movimentos."],
    ),
    (
        "T20", "PIN de administrador incorreto e depois correto",
        ["2", "1234", "2", "9999", "5", "3"],
        ["PIN de administrador incorreto.", "1. Criar conta"],
    ),
    (
        "T21", "Listar contas",
        ["2", "9999", "2", "5", "3"],
        [
            "1001 | Conta à ordem | João Silva | 1130.75 €",
            "1002 | Conta poupança | Maria Costa | 2449.00 €",
            "1003 | Conta à ordem | Pedro Santos | 600.00 €",
        ],
    ),
    (
        "T22", "Criar conta poupança",
        ["2", "9999", "1", "2", "Ana Lopes", "1111", "50", "2", "5", "3"],
        [
            "Conta criada: 1004 | Conta poupança | Ana Lopes | 50.00 €",
            "IBAN: PT50000000000000000001004",
            "1004 | Conta poupança | Ana Lopes | 50.00 €",
        ],
    ),
    (
        "T23", "Criar conta com nome inválido",
        ["2", "9999", "1", "1", "Ana", "1111", "50", "5", "3"],
        ["Erro: O nome do titular tem de ter nome e apelido, só com letras."],
    ),
    (
        "T24", "Criar conta com PIN inválido",
        ["2", "9999", "1", "1", "Ana Lopes", "12a4", "50", "5", "3"],
        ["Erro: O PIN tem de ter 4 dígitos."],
    ),
    (
        "T25", "Criar conta com tipo inválido",
        ["2", "9999", "1", "3", "5", "3"],
        ["Erro: Tipo de conta inválido."],
    ),
    (
        "T26", "Eliminar conta com saldo",
        ["2", "9999", "3", "1001", "5", "3"],
        ["Erro: Só é possível eliminar contas com saldo zero."],
    ),
    (
        "T27", "Eliminar conta inexistente",
        ["2", "9999", "3", "5555", "5", "3"],
        ["Erro: Conta não encontrada."],
    ),
    (
        "T28", "Eliminar conta com saldo zero",
        ["2", "9999", "1", "1", "Rui Costa", "2222", "0", "3", "1004", "2", "5", "3"],
        ["Conta eliminada."],
    ),
    (
        "T29", "Desbloquear conta bloqueada",
        [
            "1", "1001", "0000", "0000", "0000", "2", "9999", "4", "1001", "5", "1", "1001",
            "1234", "6", "3",
        ],
        [
            "PIN incorreto. A conta foi bloqueada.",
            "Conta desbloqueada.",
            "Bem-vindo(a), João Silva.",
        ],
    ),
    (
        "T30", "Desbloquear conta não bloqueada",
        ["2", "9999", "4", "1002", "5", "3"],
        ["Erro: A conta não está bloqueada."],
    ),
    (
        "T31", "Opções inválidas nos três menus",
        ["7", "1", "1001", "1234", "9", "6", "2", "9999", "x", "5", "3"],
        ["Opção inválida.", "Opção inválida.", "Opção inválida."],
    ),
    (
        "T32", "Sair do programa",
        ["3"],
        ["Obrigado por utilizar o nosso multibanco."],
    ),
    (
        "T33", "Transferência para IBAN com formato inválido",
        ["1", "1001", "1234", "4", "PT5012345", "100", "6", "3"],
        ["Erro: IBAN inválido."],
    ),
    (
        "T34", "Depósito de valor negativo",
        ["1", "1001", "1234", "3", "-10", "6", "3"],
        ["Erro: O valor tem de ser positivo e ter no máximo 2 casas decimais."],
    ),
    (
        "T35", "Criar conta com saldo inicial de 3 casas decimais",
        ["2", "9999", "1", "1", "Ana Lopes", "1111", "10.555", "5", "3"],
        ["Erro: O saldo inicial tem de ser zero ou positivo, com o máximo de 2 casas decimais."],
    ),
]



def run_program(folder: Path, inputs: list[str]) -> tuple[int, str, str]:
    """
    Executa o main.py da pasta indicada com as respostas fornecidas.

    Args:
        folder (Path): Pasta onde está o main.py.
        inputs (list[str]): Respostas a dar ao programa, uma por linha.

    Returns:
        tuple[int, str, str]: Código de saída, saída normal e saída de erros.
    """
    try:
        # Força UTF-8 no programa testado: no Windows, a saída redirecionada
        # usaria a codificação do sistema (cp1252) e os acentos ficariam ilegíveis
        environment = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
        process = subprocess.run(
            [sys.executable, "main.py"],
            cwd=folder,
            input="\n".join(inputs) + "\n",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
            timeout=TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired:
        return -1, "", "O programa não terminou dentro do tempo limite."
    return process.returncode, process.stdout or "", process.stderr or ""


def check_scenario(output: str, expected: list[str]) -> str | None:
    """
    Verifica se as mensagens esperadas aparecem na saída, pela ordem indicada.

    Args:
        output (str): Saída do programa.
        expected (list[str]): Mensagens esperadas.

    Returns:
        str | None: A primeira mensagem em falta, ou None se todas aparecerem.
    """
    position = 0
    for message in expected:
        index = output.find(message, position)
        if index < 0:
            return message
        position = index + len(message)
    return None


def main() -> None:
    """Corre todos os cenários e apresenta o resumo."""
    if len(sys.argv) != 2:
        print("Uso: python corrigir_cenarios.py multibanco")
        sys.exit(1)

    folder = Path(sys.argv[1])
    if not (folder / "main.py").is_file():
        print(f"Erro: não existe main.py em {folder}")
        sys.exit(1)

    passed = 0
    for scenario_id, description, inputs, expected in S:
        exit_code, output, errors = run_program(folder, inputs)
        missing = check_scenario(output, expected)
        if missing is None and exit_code == 0:
            passed += 1
            print(f"OK     {scenario_id}  {description}")
            continue

        print(f"FALHA  {scenario_id}  {description}")
        if missing is not None:
            print(f"         Mensagem em falta: {missing}")
        if exit_code != 0:
            last_error = errors.strip().splitlines()[-1] if errors.strip() else "sem detalhes"
            print(f"         O programa terminou com erro (código {exit_code}): {last_error}")

    print()
    print(f"Cenários OK: {passed} de {len(S)}")


if __name__ == "__main__":
    main()
