from .arquivo_de_midia import ArquivoDeMidia
# from Streaming.usuario import Usuario

class Playlist:
    

    def __init__(
            self, nome: str, usuario,
            itens: list[ArquivoDeMidia]):
        self.nome = nome
        self.usuario = usuario
        self.itens = itens
        self.reproducoes = 0

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def reproduzir(self):
        self.reproducoes += 1
        # print('Músicas reproduzidas')
        for i in self.itens:
            i.reproducoes += 1
            i.reproduzir()

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
         self.usuario == other.usuario and
         self.itens == other.itens)
        
    def __str__(self):
        return f'{self.nome}: {self.itens}'    

    def __repr__(self):
        return f'{self.nome}: {self.itens}' 