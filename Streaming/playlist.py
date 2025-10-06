from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.usuario import Usuario

class Playlist:
    reproducoes = 0

    def __init__(
            self, nome: str, usuario: Usuario,
            itens: list[ArquivoDeMidia]):
        self.nome = nome
        self.usuario = usuario
        self.itens = itens

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def reproduzir(self):
        self.reproducoes += 1
        print('Músicas reproduzidas')
        for i in self.itens:
            print(i)
            i.reproducoes += 1

    def __add__(self, other):
        return Playlist(
            self.nome,
            self.usuario,
            self.itens + other.itens,
            self.reproducoes + other.reproducoes,
        )

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, index):
        return self.itens[index]

    def __eq__(self, other):
        (self.nome == other.nome and
         self.usario == other.usuario and
         self.itens == other.itens)