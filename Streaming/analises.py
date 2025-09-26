from arquivo_de_midia import ArquivoDeMidia
from playlist import Playlist
from musica import Musica
from usuario import Usuario

class Analises:

    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int) -> list[Musica]:
        pass

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]) -> Playlist:
        pass

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]) -> Usuario:
        pass

    @staticmethod
    def media_avaliacoes(musicas: list[Musica]) -> dict[str, float]:
        pass

    @staticmethod
    def total_reproducoes(usuarios: list[Usuario]) -> int:
        pass