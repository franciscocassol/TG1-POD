from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast


class Usuario:
    qntd_instancias = 0
    historico = []
    musicas = ()
    podcasts = ()


    def __init__(self, nome, playlists):
        self.qntd_instancias += 1
        self.nome = nome
        self.playlists = playlists

        Usuario.initialize_playlists()
        

    def initialize_playlists(self):  
        for p in self.playlists:
            self.criar_playlist(p)
            for item in p.itens:
                if(isinstance(item, Musica)):
                    self.musicas.add(item)
                elif(isinstance(item, Podcast)):
                    self.poscasts.add(item)
                      

    def ouvir_midia(midia: ArquivoDeMidia):
        print(f'teste - ouviu musica {midia}')
        pass

    def criar_playlist(self, nome):
        self.playlists.append(Playlist(nome, self, [], 0))
        return self.playlists[-1]
        pass
        

    def __str__(self):
        str_final = ''
        for p in self.playlists:
            str_final += ", ".join(p)
        return (str_final)


if __name__ == "__main__":
    user = Usuario('a', [])
    print(user)
