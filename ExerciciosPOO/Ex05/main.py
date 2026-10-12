from book import Book


def main() -> None:
    try:
        book_one = Book("Os Maias", "9789720046406", "Romance")
        book_two = Book("Manual de Python", "9789898927149")
    except ValueError as error:
        print(f"Erro: {error}")
        return

    for book in (book_one, book_two):
        print(book.title, book.isbn, book.genre)

    try:
        book_one.isbn = "12345"
    except ValueError as error:
        print(f"Erro: {error}")

    try:
        Book("Livro Novo", "978ABC")
    except ValueError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
