from .arquivo_de_midia import ArquivoDeMidia
# from Streaming.usuario import Usuario

class Playlist:
    

    def __init__(
            self, nome: str, usuario,
            itens: list[ArquivoDeMidia], reproducoes: int = 0):
        self.nome = nome
        self.usuario = usuario
        self.itens = itens
        self.reproducoes = reproducoes

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        self.itens.remove(midia)

    def reproduzir(self):
        self.reproducoes += 1
        # print('Músicas reproduzidas')
        for i in self.itens:
            i.reproducoes += 1
            i.reproduzir()

    def __add__(self, other):
        set1 = set(self.itens)
        set2 = set(other.itens)
        uniao_set = list(set1.union(set2))
        
        return Playlist(
            self.nome,
            self.usuario,
            uniao_set,
            self.reproducoes + other.reproducoes
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