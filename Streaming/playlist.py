from .arquivo_de_midia import ArquivoDeMidia


class Playlist:
    """
    Classe que representa uma playlist de músicas e podcasts.

    Atributos:
        nome (str): O nome da playlist.
        usuario (Usuario): O objeto Usuario que criou a playlist.
        itens (list[ArquivoDeMidia]): Uma lista de objetos ArquivoDeMidia.
        reproducoes (int): Contador de reproduções da playlist.
    """

    def __init__(
            self, nome: str, usuario,
            itens: list[ArquivoDeMidia], reproducoes: int = 0):
        self.nome = nome
        self.usuario = usuario
        self.itens = itens
        self.reproducoes = reproducoes
        """
        Inicializa uma nova instância da classe Playlist.

        Args:
            nome (str): O nome da playlist.
            usuario (Usuario): O criador da playlist.
            itens (list[ArquivoDeMidia]): A lista inicial de mídias.
            reproducoes (int): O contador de reproduções.
        """
        

    def adicionar_midia(self, midia: ArquivoDeMidia):
        """
        Adiciona um ArquivoDeMidia à lista de itens da playlist.

        Args:
            midia (ArquivoDeMidia): O objeto de mídia a ser adicionado.
        """
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        """
        Remove um ArquivoDeMidia da lista de itens da playlist.

        Args:
            midia (ArquivoDeMidia): O objeto de mídia a ser removido.
        """
        self.itens.remove(midia)

    def reproduzir(self, user):
        """
        Reproduz todas as mídias da playlist, incrementando o contador
        de reproduções da playlist e de cada item.

        Args:
            user (Usuario): O usuário que está reproduzindo a playlist.
        """
        self.reproducoes += 1

        for i in self.itens:
            user.ouvir_midia(i)


    def __add__(self, other):
        """
        Permite a concatenação de duas playlists, criando uma nova playlist
        sem itens duplicados.

        Args:
            other (Playlist): A outra playlist a ser concatenada.

        Returns:
            Playlist: Uma nova playlist com os itens das duas playlists originais.
        """
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
        """
        Retorna o número de itens na playlist.

        Returns:
            int: O número de mídias na playlist.
        """
        return len(self.itens)

    def __getitem__(self, index):
        """
        Permite o acesso aos itens da playlist por índice (ex: playlist[0]).

        Args:
            index (int): O índice do item desejado.

        """
        return self.itens[index]

    def __eq__(self, other):
        """
        Compara se duas playlists são iguais com base no nome, usuário e itens.

        Args:
            other (object): O objeto a ser comparado.
        """
        (self.nome == other.nome and
         self.usuario == other.usuario and
         self.itens == other.itens)
        
    def __str__(self):
        """
        Retorna a representação da string do objeto.

        Returns:
            str: O nome da playlist e seus itens.
        """
        return f'{self.nome}: {self.itens}'    

    def __repr__(self):
        """
        Retorna a representação do objeto para desenvolvedores.

        Returns:
            str: O nome da playlist e seus itens.
        """

        return f'{self.nome}: {self.itens}' 