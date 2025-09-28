from abc import ABC, abstractmethod


class ArquivoDeMidia(ABC):
    reproducoes = 0

    def __init__(
            self, titulo: str, duracao: int,
            artista: str):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista

    def reproduzir(self):
        print(f'Título: {self.titulo}')
        print(f'Duração: {self.duracao}')
        print(f'Artista: {self.artista}')
        # print(f'Reproduções: {self.reproducoes}')

    def __eq__(self, other):
        self.titulo == other.titulo and self.artista == other.artista