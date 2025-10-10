from .arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    """
    Classe que representa uma música, sendo uma subclasse de ArquivoDeMidia.

    Atributos:
        genero (str): O gênero musical da música (ex: 'Rock', 'Pop').
        avaliacoes (list[int]): Uma lista de notas de avaliação de 0 a 5.
        reproducoes (int): Contador de execuções da música.
    """
    

    def __init__(
            self, titulo, duracao, artista,
            genero: str, avaliacoes: list[int]):
        super().__init__(titulo, duracao, artista)
        self.genero = genero
        self.avaliacoes = avaliacoes

        self.reproducoes = 0
        """
        Inicializa uma nova instância da classe Musica.

        Args:
            titulo (str): O nome da música.
            duracao (int): A duração da música em segundos.
            artista (str): O nome do artista da música.
            genero (str): O gênero da música.
            avaliacoes (list[int]): Lista inicial de notas de avaliação.
        """

    def __eq__(self, other):
        """
        Compara se dois objetos Musica são iguais com base no título e artista.
        
        Args:
            other (object): O objeto a ser comparado.
        """
        if isinstance(other, Musica):
            return self.titulo == other.titulo and self.artista == other.artista
        return False

    def __hash__(self):
        """
        Gera um hash para o objeto, permitindo que seja usado em sets e dicionários.
        """
        return hash((self.titulo, self.artista))


    def avaliar(self, nota):
        """
        Adiciona uma nota de avaliação à lista de avaliações da música.

        Args:
            nota (int): A nota de avaliação (de 0 a 5).
        """
        self.avaliacoes.append(nota)

    def __str__(self):
        """
        Retorna a representação da string do objeto (título).
        
        Returns:
            str: O título da música.
        """
        return f'{self.titulo}'
    
    def __repr__(self):
        """
        Retorna a representação do objeto para desenvolvedores (título).
        
        Returns:
            str: O título da música.
        """
        return f'{self.titulo}'