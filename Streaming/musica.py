from .arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    

    def __init__(
            self, titulo, duracao, artista,
            genero: str, avaliacoes: list[int]):
        super().__init__(titulo, duracao, artista)
        self.genero = genero
        self.avaliacoes = avaliacoes

        self.reproducoes = 0

    def __eq__(self, other):
        if isinstance(other, Musica):
            return self.titulo == other.titulo and self.artista == other.artista
        return False

    def __hash__(self):
        return hash((self.titulo, self.artista))


    def avaliar(self, nota):
        self.avaliacoes.append(nota)

    def __str__(self):
        return f'{self.titulo}'
    
    def __repr__(self):
        return f'{self.titulo}'