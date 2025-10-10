from abc import ABC, abstractmethod


class ArquivoDeMidia(ABC):
    """
    Classe abstrata que representa uma mídia genérica.
    Músicas e podcasts devem herdar dessa classe.
    """    

    @abstractmethod
    def __init__(
            self, titulo: str, duracao: int,
            artista: str):
        """
        Inicializa uma mídia com título, duração e artista.

        Args:
            titulo (str): Título da mídia.
            duracao (int): Duração em segundos.
            artista (str): Nome do artista.
        """
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista

        self.reproducoes = 0

    def reproduzir(self):
        """
        Exibe informações da mídia e simula sua reprodução.
        """
        print()
        print(f'Título: {self.titulo}')
        print(f'Duração: {self.duracao}')
        print(f'Artista: {self.artista}')
        print(f'Reproduções: {self.reproducoes}')

    def __eq__(self, other):
        """
        Compara duas mídias pelo título e artista.

        Args:
            other (ArquivoDeMidia): Outro objeto de mídia.

        Returns:
            bool: True se título e artista forem iguais, False caso contrário.
        """
        self.titulo == other.titulo and self.artista == other.artista

    def __str__(self):
        return f'{self.titulo}'

    def __repr__(self):
        return f'{self.titulo}'
