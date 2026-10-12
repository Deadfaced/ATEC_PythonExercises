from online_resource import OnlineResource


def main() -> None:
    resource = OnlineResource("Guia de Python", "https://docs.python.org")
    print(f"{resource.title}: {resource.url}")

    invalid_resources = [
        ("Curso de Git", "www.git-scm.com"),
        ("", "https://exemplo.pt"),
    ]

    for title, url in invalid_resources:
        try:
            OnlineResource(title, url)
        except ValueError as error:
            print(f"Erro: {error}")


if __name__ == "__main__":
    main()
