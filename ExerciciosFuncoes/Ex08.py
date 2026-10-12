def calculate_attachment_size(content: str) -> int:
    if content == "":
        raise ValueError("o anexo está vazio.")

    return len(content.encode("utf-8"))


def main():
    try:
        print(f"Tamanho: {calculate_attachment_size('Olá')} bytes")
        print(f"Tamanho: {calculate_attachment_size('')} bytes")
    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()