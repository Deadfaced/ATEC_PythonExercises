def close_order(total: float, lines: list[str]) -> None:
    """
    Tenta somar 5.0 ao total e acrescenta "FECHADA" à lista.

    O valor de total não muda fora da função porque float é imutável.
    Já a lista muda porque list é mutável e append() altera o mesmo objeto.
    """
    total += 5.0
    lines.append("FECHADA")


def add_shipping(total: float) -> float:
    """
    Devolve o total com 5.0 de portes adicionados.
    """
    return total + 5.0


def main():
    order_total = 100.0
    order_lines = ["Caderno", "Caneta"]

    print("Antes:", order_total, order_lines)

    close_order(order_total, order_lines)

    print("Depois:", order_total, order_lines)

    order_total = add_shipping(order_total)

    print("Total actualizado:", order_total)


if __name__ == "__main__":
    main()