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

    @staticmethod
    def create_match_playlists(u1: Usuario, u2: Usuario):
        musicas_compativeis = []
        musicas_em_comum = set(u1.historico.keys()) & set(u2.historico.keys())

        if not musicas_em_comum:
            print("Não há musicas em comum no historico dos usuarios para criar um match")
            return None
        
        for musica in musicas_em_comum:
            avaliacoes_u1 = u1.historico.get(musica, [])
            avaliacoes_u2 = u2.historico.get(musica, [])

            if avaliacoes_u1 and avaliacoes_u2:
                media_u1 = sum(avaliacoes_u1) / len(avaliacoes_u1)
                media_u2 = sum(avaliacoes_u1) / len(avaliacoes_u2)
            
            if abs(media_u1 - media_u2) <= 1:
                musicas_compativeis.append(musica)

        if not musicas_compativeis:
            print("Não há musicas com avaliações compativeis para criar um match.")
            return None
        
        return Playlist(
            nome = f"Match de {u1.nome} e {u2.nome}",
            user = u1
            itens= musicas_compativeis
        )


    