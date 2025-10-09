from .arquivo_de_midia import ArquivoDeMidia
from .playlist import Playlist
from .musica import Musica
from .podcast import Podcast


class Usuario:
    qntd_instancias = 0
    

    def __init__(self, nome, playlists_names):
        Usuario.qntd_instancias += 1
        self.nome = nome
        self.playlists_names = playlists_names
        self.playlists = []

        self.historico = []
        self.musicas = set()
        self.podcasts = set()

        self.initialize_playlists()

    def initialize_playlists(self):
        for p in self.playlists_names:
            self.criar_playlist(p)

    
    def inicialize_media(self):
        for p in self.playlists:
            for item in p.itens:
                if(isinstance(item, Musica)):
                    self.musicas.add(item)
                elif(isinstance(item, Podcast)):
                    self.podcasts.add(item)


    def ouvir_midia(self, midia: ArquivoDeMidia):
        midia.reproducoes += 1
        midia.reproduzir()

    def criar_playlist(self, nome):
        self.playlists.append(Playlist(nome, self, []))
        return self.playlists[-1]

    def __str__(self):
        return f'{self.nome}'

    def __repr__(self):
        return f'User: {self.nome}\nPlaylists: {self.playlists}'



