from .arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    reproducoes = 0

    def __init__(
            self, titulo, duracao, artista,
            episodio: str, temporada: int,):
        super().__init__(titulo, duracao, artista)
        self.episodio = episodio
        self.temporada = temporada

    
    def __eq__(self, other):
        if isinstance(other, Podcast):
            return self.titulo == other.titulo and self.artista == other.artista
        return False

    def __hash__(self):
        return hash((self.titulo, self.artista))

    def __str__(self):
        return f'{self.titulo}'
    
    def __repr__(self):
        return f'{self.titulo}'