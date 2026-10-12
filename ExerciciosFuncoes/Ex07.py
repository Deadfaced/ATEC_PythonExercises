def calculate_average_price(total: float, quantity: int) -> float:
    print("Ligação à base de dados estabelecida")

    try:
        return total / quantity
    finally:
        print("Ligação encerrada e recursos libertados")


def main():
    try:
        calculate_average_price(100.0, 0)
    except ZeroDivisionError:
        print("Erro: não é possível calcular o preço médio com quantidade zero.")


if __name__ == "__main__":
    main()