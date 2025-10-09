from .arquivo_de_midia import ArquivoDeMidia
from .playlist import Playlist
from .musica import Musica
from .usuario import Usuario

class Analises:

    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int) -> list[Musica]:
        musicas_ordenadas = sorted(musicas, key=lambda musica: musica.reproducoes, reverse=True)
        return musicas_ordenadas[:top_n]

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]) -> Playlist:
        if not playlists:
            return None
        top_playlist = max(playlists, key=lambda playlist: playlist.reproducoes)
        return top_playlist

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]) -> Usuario:
        if not usuarios:
            return None
        
        usuario_ativo = max(usuarios, key=lambda usuario: len(usuario.historico))
        return usuario_ativo
    

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
            user = u1,
            itens= musicas_compativeis
        )


    