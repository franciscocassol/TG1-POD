from arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    reproducoes = 0

    def __init__(
            self, titulo, duracao, artista,
            genero: str, avaliacoes: list[int], avaliar: int):
        super().__init__(titulo, duracao, artista)
        self.genero = genero
        self.avaliacoes = avaliacoes

        self.avaliacoes.append(avaliar)