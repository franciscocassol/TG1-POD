from .usuario import Usuario
from .musica import Musica
from .podcast import Podcast
from .playlist import Playlist
from pathlib import Path


class LeArquivo:
    """
    Classe responsável por ler arquivos de texto e criar objetos de Usuário, Músicas, Podcasts
    e Playlists. Possui métodos estáticos para leitura e registro de erros.
    """

    @staticmethod
    def log_error(e, msg=""):
        """
        Registra erros em um arquivo de log 'logs/erros.log'.

        Args:
            e (Exception | str): Objeto de exceção ou mensagem de erro.
            msg (str, opcional): Mensagem adicional para contextualizar o erro.
        """
        log_dir = Path(__file__).parent / "logs"  
        log_dir.mkdir(exist_ok=True) 

        log_path = log_dir / "erros.log"  
        with open(log_path, 'a', encoding='utf-8') as log:
            log.write(f'{msg} ERRO: {e}\n')

    def read_file(file_name):
        """
        Lê o arquivo de entrada e separa seu conteúdo em usuários, músicas, podcasts e playlists.

        Args:
            file_name (str): Nome do arquivo a ser lido.

        Returns:
            tuple: Quatro listas contendo objetos:
                - users_list (list[Usuario])
                - songs_list (list[Musica])
                - podcasts_list (list[Podcast])
                - playlists_list (list[Playlist])
        """

        try:
            with open(f"{file_name}", "r", encoding='utf-8') as file:
                content = file.readlines()
        except Exception as e:
            LeArquivo.log_error(e, "Erro ao abrir o arquivo")
            return [], [], []  

        actual = None
        key_word = False

        user_lines, song_lines, podcast_lines, playlist_lines = [], [], [], []

        for num_linha, line in enumerate(content,1):
            
            try:
                line = line.strip()
                words = line.split()
                key_word = bool(words) and words[0] == '#'

                if key_word:
                    actual = words[1]

                if actual:
                    match (actual):
                        case 'Usuários': user_lines.append(line)
                        case 'Músicas': song_lines.append(line)
                        case 'Podcasts': podcast_lines.append(line)
                        case 'Playlists': playlist_lines.append(line)
                        case _: 'erro'
            except Exception as e:
                LeArquivo.log_error(e, f"Linha {num_linha}")


        users_list = LeArquivo.read_user(user_lines)
        songs_list = LeArquivo.read_song(song_lines)
        podcasts_list = LeArquivo.read_podcast(podcast_lines)

        # dicionarios com strings de chave e objetos de valor
        users_dict = {u.nome: u for u in users_list}
        songs_dict = {t.titulo: t for t in songs_list}
        podcasts_dict = {t.titulo: t for t in podcasts_list}

        # concatena dicionarios
        dict_midias = songs_dict | podcasts_dict

        playlists_list = LeArquivo.read_playlist(playlist_lines, users_dict, dict_midias)

        for u in users_list:
            u.inicialize_media()

        return users_list, songs_list, podcasts_list, playlists_list

    @staticmethod
    def read_user(lines):
        """
        Converte linhas de usuários em objetos Usuario.

        Args:
            lines (list[str]): Linhas correspondentes a usuários.

        Returns:
            list[Usuario]: Lista de objetos Usuario.
        """
        users_list = []

        for i in range(len(lines) - 2):
            words = lines[i].strip().split(': ')
            if words and words[0] == '- nome':

                usuario_existente = any(u.nome == words[1] for u in users_list) 
                if usuario_existente:
                    LeArquivo.log_error(f"O usuário '{words[1]}' já existe no sistema")
                    continue

                next_line = lines[i+1]

                playlist = next_line.split(":")[1].strip()[1:-1].split(",")
                playlist = [s.strip() for s in playlist]

                users_list.append(Usuario(words[1], playlist))
        return users_list

    @staticmethod
    def read_song(lines):
        """
        Converte linhas de músicas em objetos Musica.

        Args:
            lines (list[str]): Linhas correspondentes a músicas.

        Returns:
            list[Musica]: Lista de objetos Musica.
        """
        songs_list = []

        for i in range(len(lines) - 2):
            words = lines[i].strip().split(': ')
            if words and words[0] == '- titulo':

                artist_line = lines[i+1]
                artist = artist_line.strip().split(": ")[1]

                genre_line = lines[i+2]
                genre = genre_line.strip().split(": ")[1]

                duration_line = lines[i+3]
                duration = int(duration_line.strip().split(": ")[1])

                songs_list.append(
                    Musica(words[1], duration, artist, genre, []))
        return songs_list
    
    @staticmethod
    def read_podcast(lines):
        """
        Converte linhas de podcasts em objetos Podcast.

        Args:
            lines (list[str]): Linhas correspondentes a podcasts.

        Returns:
            list[Podcast]: Lista de objetos Podcast.
        """
        podcasts_list = []

        for i in range(len(lines) - 2):
            words = lines[i].strip().split(': ')
            if words and words[0] == '- titulo':

                season_line = lines[i+1]
                season = season_line.strip().split(": ")[1]

                episode_line = lines[i+2]
                episode = int(episode_line.strip().split(": ")[1])

                host_line = lines[i+3]
                host = host_line.strip().split(": ")[1]

                duration_line = lines[i+4]
                duration = int(duration_line.strip().split(": ")[1])

                podcasts_list.append(
                    Podcast(words[1], duration, host, episode, season))
        return podcasts_list

    def read_playlist(lines, users_dict, dict_midias):
        """
        Converte linhas de playlists em objetos Playlist, associando usuários e mídias.

        Args:
            lines (list[str]): Linhas correspondentes a playlists.
            users_dict (dict[str, Usuario]): Dicionário de usuários para associação.
            dict_midias (dict[str, ArquivoDeMidia]): Dicionário de mídias (músicas + podcasts).

        Returns:
            list[Playlist]: Lista de objetos Playlist.
        """

        playlists_list = []

        for i in range(len(lines) - 2):
            words = lines[i].strip().split(': ')
            if words and words[0] == '- nome':

                user_line = lines[i+1]
                user = user_line.strip().split(": ")[1]

                itens_line = lines[i+2]

                itens = itens_line.split(":")[1].strip()[1:-1].split(",")
                itens = [s.strip() for s in itens]
                
                user_object = users_dict.get(user)
                playlists_dict = {p.nome: p for p in user_object.playlists}
                playlist_object = playlists_dict.get(words[1])

                for i in itens:
                    midia_object = dict_midias.get(i)
                    if midia_object is None:
                        LeArquivo.log_error(f"Música '{i}' inexistente na playlist '{playlist_object.nome}' do usuário '{user}'")
                    playlist_object.adicionar_midia(midia_object)
                playlists_list.append(playlist_object)
        return playlists_list

