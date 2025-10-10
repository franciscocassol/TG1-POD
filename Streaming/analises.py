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
        Cria uma playlist de 'match' entre dois usuários, baseada nas músicas que ambos ouviram
        e cujas avaliações médias são compatíveis (diferença <= 1).
        """

        musicas_compativeis = []
        musicas_em_comum = set(m.titulo for m in u1.musicas) & set(m.titulo for m in u2.musicas)

        if not musicas_em_comum:
            print("Não há músicas em comum no histórico dos usuários para criar um match.")
            return None

        # dicionários de avaliações por música
        avaliacoes_u1 = {m.titulo: m.avaliacoes for m in u1.musicas}
        avaliacoes_u2 = {m.titulo: m.avaliacoes for m in u2.musicas}

        for titulo in musicas_em_comum:
            aval1 = avaliacoes_u1.get(titulo, [])
            aval2 = avaliacoes_u2.get(titulo, [])

            # se algum não avaliou, ignora
            if not aval1 or not aval2:
                continue  

            media1 = sum(aval1) / len(aval1)
            media2 = sum(aval2) / len(aval2)

            if abs(media1 - media2) <= 1:
                # pegar o objeto Musica original do usuário 1
                musica_obj = next((m for m in u1.musicas if m.titulo == titulo), None)
                if musica_obj:
                    musicas_compativeis.append(musica_obj)

        if not musicas_compativeis:
            print("Não há músicas com avaliações compatíveis para criar um match.")
            return None

        return Playlist(
            nome=f"Match de {u1.nome} e {u2.nome}",
            usuario=u1,
            itens=musicas_compativeis
        )


    