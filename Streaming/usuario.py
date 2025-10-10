from .arquivo_de_midia import ArquivoDeMidia
from .playlist import Playlist
from .musica import Musica
from .podcast import Podcast


class Usuario:
    """
    Representa um usuário do sistema, que possui playlists, histórico de reprodução
    e coleções de músicas e podcasts.

    Atributos de classe:
        qntd_instancias (int): Conta o número total de instâncias de Usuario criadas.
    """

    qntd_instancias = 0
    

    def __init__(self, nome, playlists_names):
        """
        Inicializa um novo usuário.

        Args:
            nome (str): Nome do usuário.
            playlists_names (list[str]): Lista de nomes das playlists iniciais.
        """
         
        Usuario.qntd_instancias += 1
        self.nome = nome
        self.playlists_names = playlists_names
        self.playlists = []

        self.historico = {}
        self.musicas = set()
        self.podcasts = set()

        self.initialize_playlists()

    def initialize_playlists(self):
        """
        Inicializa as playlists do usuário com base nos nomes fornecidos
        em playlists_names.
        """
        for p in self.playlists_names:
            self.criar_playlist(p)

    
    def inicialize_media(self):
        """
        Popula os conjuntos de músicas e podcasts do usuário a partir das playlists existentes.
        """
        for p in self.playlists:
            for item in p.itens:
                if(isinstance(item, Musica)):
                    self.musicas.add(item)
                elif(isinstance(item, Podcast)):
                    self.podcasts.add(item)


    def ouvir_midia(self, midia: ArquivoDeMidia):
        """
        Adiciona uma mídia ao histórico do usuário e incrementa o contador
        de reproduções da mídia.

        Args:
            midia (ArquivoDeMidia): Objeto de mídia que será reproduzido.
        """
        self.historico[midia.titulo] = midia
        midia.reproducoes += 1
        midia.reproduzir()

    def criar_playlist(self, nome):
        """
        Cria uma nova playlist para o usuário.

        Args:
            nome (str): Nome da nova playlist.

        Returns:
            Playlist: A playlist recém-criada.
        """
        self.playlists.append(Playlist(nome, self, []))
        return self.playlists[-1]
    
    def concatenar_playlists(self, p1, p2):
        """
        Concatena duas playlists do usuário, removendo a segunda da lista
        de playlists e substituindo a primeira pela playlist resultante.

        Args:
            p1 (Playlist): Primeira playlist.
            p2 (Playlist): Segunda playlist, que será removida.

        Returns:
            Playlist: Nova playlist resultante da concatenação.
        """
        self.playlists.remove(p2)
        new = p1 + p2
        self.playlists[self.playlists.index(p1)] = new
        return new
    
    def __iter__(self):
        """
        Permite iterar sobre as playlists do usuário.

        Returns:
            iterator: Iterador sobre a lista de playlists.
        """
        return iter(self.playlists)

    def __str__(self):
        return f'{self.nome}'

    def __repr__(self):
        return f'User: {self.nome}\nPlaylists: {self.playlists}'



