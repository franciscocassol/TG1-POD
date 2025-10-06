from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist


class Usuario:
    qntd_instancias = 0
    historico = []

    def __init__(self, nome, playlists):
        self.qntd_instancias += 1
        self.nome = nome
        self.playlists = playlists

        for p in playlists:
            self.criar_playlist(p)

    def ouvir_midia(midia: ArquivoDeMidia):
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
