import sys


def main():
    try:
        vat_rate = int(sys.argv[1])
    except ValueError:
        print("Erro: a taxa de IVA deve ser um número inteiro.")
        sys.exit(1)

    print(f"Ferramenta iniciada com IVA de {vat_rate}%")
    sys.exit(0)


if __name__ == "__main__":
    main()