import sys

from music_player import MusicPlayer


def main() -> None:
    player = MusicPlayer()

    while True:
        print("1. Carregar música")
        print("2. Reproduzir")
        print("3. Sair")
        option = input("Opção: ").strip()

        try:
            if option == "1":
                title = input("Título da música: ")
                player.load_song(title)
                print("Música carregada.")
            elif option == "2":
                player.play()
            elif option == "3":
                print("A encerrar.")
                sys.exit(0)
            else:
                print("Opção inválida.")
        except (ValueError, RuntimeError) as error:
            print(f"Erro: {error}")


if __name__ == "__main__":
    main()
