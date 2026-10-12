from typing import Optional


def add_to_cart(item: str, cart: Optional[list] = None) -> list:
    if cart is None:
        cart = []

    cart.append(item)
    return cart


def main():
    cart_a = add_to_cart("Caderno")
    cart_b = add_to_cart("Caneta")
    cart_a = add_to_cart("Borracha", cart_a)

    print("Carrinho A:", ["Caderno"])
    print("Carrinho B:", cart_b)
    print("Carrinho A actualizado:", cart_a)


if __name__ == "__main__":
    main()