from Streaming.arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    reproducoes = 0

    def __init__(
            self, titulo, duracao, artista,
            episodio: str, temporada: int,):
        super().__init__(titulo, duracao, artista)
        self.episodio = episodio
        self.temporada = temporada