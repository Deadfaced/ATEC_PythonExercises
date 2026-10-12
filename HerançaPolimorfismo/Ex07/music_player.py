from song import Song


class MusicPlayer:
    def __init__(self) -> None:
        self.__current_song: Song | None = None

    def get_current_song(self) -> Song | None:
        return self.__current_song

    def load_song(self, title: str) -> None:
        self.__current_song = Song(title)

    def play(self) -> None:
        if self.__current_song is None:
            raise RuntimeError("Nenhuma música carregada.")
        print(f"A reproduzir: {self.__current_song!r}")
