from .arquivo_de_midia import ArquivoDeMidia
from .playlist import Playlist
from .musica import Musica
from .usuario import Usuario

class Analises:
    """
        Classe estática para análises de usuários, playlists e músicas.
        Todos os métodos são estáticos e não dependem de instâncias.
    """

    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int) -> list[Musica]:
        """
        Retorna as top N músicas mais reproduzidas.

        Args:
            musicas (list[Musica]): Lista de objetos Musica.
            top_n (int): Quantidade de músicas desejadas.

        Returns:
            list[Musica]: Lista das N músicas mais reproduzidas.
        """
        musicas_ordenadas = sorted(musicas, key=lambda musica: musica.reproducoes, reverse=True)
        return musicas_ordenadas[:top_n]

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]) -> Playlist:
        """
        Retorna a playlist mais popular, com base no número de reproduções.

        Args:
            playlists (list[Playlist]): Lista de playlists.

        Returns:
            Playlist: Playlist com mais reproduções ou None se a lista estiver vazia.
        """
        if not playlists:
            return None
        top_playlist = max(playlists, key=lambda playlist: playlist.reproducoes)
        return top_playlist

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]) -> Usuario:
        """
        Retorna o usuário mais ativo, com base na quantidade de mídias reproduzidas.

        Args:
            usuarios (list[Usuario]): Lista de usuários.

        Returns:
            Usuario: Usuário com mais entradas no histórico ou None se a lista estiver vazia.
        """
        if not usuarios:
            return None
        
        usuario_ativo = max(usuarios, key=lambda usuario: len(usuario.historico))
        return usuario_ativo
    

    @staticmethod
    def media_avaliacoes(musicas: list[Musica]) -> dict[str, float]:
        """
        Calcula a média das avaliações de cada música.

        Args:
            musicas (list[Musica]): Lista de músicas.

        Returns:
            dict[str, float]: Dicionário com título da música como chave e média das avaliações como valor.
                              Caso não haja avaliações, a média padrão é 5.
        """
        medias = {}
        for musica in musicas:
            if len(musica.avaliacoes) != 0:
                media = sum(musica.avaliacoes)/len(musica.avaliacoes)
                medias[musica.titulo] = media
            else:
                medias[musica.titulo] = 5
        return medias

    @staticmethod
    def total_reproducoes(usuarios: list[Usuario]) -> int:
        """
        Calcula o total de mídias reproduzidas por todos os usuários.

        Args:
            usuarios (list[Usuario]): Lista de usuários.

        Returns:
            int: Total de entradas no histórico de todos os usuários.
        """
        total = 0
        for usuario in usuarios:
            total += len(usuario.historico)
        return total

    @staticmethod
    def create_match_playlists(u1: Usuario, u2: Usuario):
        """
        Cria uma playlist de "match" entre dois usuários, baseada nas músicas que ambos ouviram
        e cujas avaliações médias são compatíveis (diferença <= 1).

        Args:
            u1 (Usuario): Primeiro usuário.
            u2 (Usuario): Segundo usuário.

        Returns:
            Playlist | None: Playlist com músicas compatíveis ou None caso não haja músicas compatíveis.
        """
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


    