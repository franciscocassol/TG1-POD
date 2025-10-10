from .arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    """
    Classe que representa um podcast, sendo uma subclasse de ArquivoDeMidia.

    Atributos:
        episodio (str): O número ou título do episódio.
        temporada (int): O número da temporada do podcast.
        reproducoes (int): Contador de execuções do podcast.
    """
    reproducoes = 0

    def __init__(
            self, titulo, duracao, artista,
            episodio: str, temporada: int,):
        super().__init__(titulo, duracao, artista)
        self.episodio = episodio
        self.temporada = temporada
        """
        Inicializa uma nova instância da classe Podcast.

        Args:
            titulo (str): O título do podcast.
            duracao (int): A duração do episódio em segundos.
            artista (str): O host do podcast.
            episodio (str): O número do episódio.
            temporada (int): O nome da temporada.
        """

    
    def __eq__(self, other):
        """
        Retorna a representação do objeto para desenvolvedores.

        Returns:
            str: O nome da playlist e seus itens.
        """
        if isinstance(other, Podcast):
            return self.titulo == other.titulo and self.artista == other.artista
        return False

    def __hash__(self):
        """
        Gera um hash para o objeto, permitindo que seja usado em sets e dicionários.

        Returns:
            int: O valor hash do objeto.
        """

        return hash((self.titulo, self.artista))

    def __str__(self):
        """
        Retorna a representação da string do objeto (título).

        Returns:
            str: O título do podcast.
        """
        
        return f'{self.titulo}'
    
    def __repr__(self):
        """
        Retorna a representação do objeto para desenvolvedores (título).

        Returns:
            str: O título do podcast.
        """
        return f'{self.titulo}'