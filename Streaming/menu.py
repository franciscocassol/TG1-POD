from .usuario import Usuario
from .le_arquivo import LeArquivo
from .analises import Analises
from pathlib import Path
import os


class Menu:
    users = []
    musicas = []
    podcasts = []
    def initialize():
        option = 0
        
        file_path = Path(__file__).resolve().parent.parent / 'config' / 'dados.md'
        

        users_list, songs_list, podcasts_list, playlists_list = LeArquivo.read_file(file_path)


        while (option != 4):
            option = Menu.select__main_option()
            match (option):
                case 1: Menu.user_options(Menu.sign_in_user(users_list), songs_list, podcasts_list, users_list, playlists_list)
                case 2: Menu.create_new_user(users_list)
                case 3: Menu.listar_usuarios(users_list)
                case _: option = 4

        print("Fim do programa!")

    def select__main_option() -> int:

        ls_options = ['Entrar como usuário', 'Criar novo usuário',
                      'Listar usuários',  'Finalizar programa']
        Menu.enumarate_logic(ls_options)

        return Menu.selection_logic(4)

    def listar_usuarios(users_list):

        Menu.enumarate_logic(users_list, False)

    def sign_in_user(users_list):

        Menu.enumarate_logic(users_list)

        users_len = len(users_list)

        option = Menu.selection_logic(users_len) - 1

        return users_list[option]

    def user_options(user, songs_list, podcasts_list, users_list, playlists_list):

        option = 0

        print(user)
        while (option != 10):
            option = Menu.select_user_option()
            match (option):
                case 1: Menu.reproduzir_musica(user)
                case 2: Menu.listar_musicas(user)
                case 3: Menu.listar_playlists(user)
                case 4: Menu.reproduzir_playlist(user)
                case 5: Menu.criar_nova_playlist(user, songs_list, podcasts_list, playlists_list)
                case 6: Menu.concatenar_playlists(user)
                case 7: Menu.gerar_relatorio(users_list, songs_list, playlists_list)
                case 8: Menu.avaliar_musica(user, songs_list)
                case 9: print(Menu.create_match_playlist_option(user, users_list ))
                case _: option = 10

    def select_user_option():
        ls_options = ['Reproduzir uma música', 'Listar músicas', 'Listar playlists',
                        'Reproduzir uma playlist', 'Criar nova playlist',
                        'Concatenar playlists', 'Gerar relatório', 'Avaliar Música', 'Criar match', 'Sair']
        Menu.enumarate_logic(ls_options)

        return Menu.selection_logic(10)
    
    def reproduzir_musica(user):
        musicas = list(user.musicas)

        Menu.enumarate_logic(musicas)

        musicas_len = len(musicas)
        option = Menu.selection_logic(musicas_len)

        user.ouvir_midia(musicas[option - 1])

    def listar_musicas(user):
        musicas = list(user.musicas)

        Menu.enumarate_logic(musicas, False)

    def listar_playlists(user):
        playlists = list(user.playlists)

        Menu.enumarate_logic(playlists, False)

    def reproduzir_playlist(user):
        playlists = list(user.playlists)

        if len(playlists) == 0:
            print('{user} não tem playlists.')
            return

        Menu.enumarate_logic(playlists)

        playlists_len = len(playlists)
        option = Menu.selection_logic(playlists_len)

        playlists[option - 1].reproduzir(user)


    def criar_nova_playlist(user, songs_list, podcasts_list, playlists_list):

        valid = False
        while not valid:
            nome_playlist = input("Digite o nome da nova playlist: ")
            playlist_esiste = any(p.nome == nome_playlist for p in user.playlists) 
            if playlist_esiste:
                print(f"Erro: O nome de usuário '{nome_playlist}' já existe.\n")
                continue
            new_playlist = user.criar_playlist(nome_playlist)
            playlists_list.append(new_playlist)
            print(f"\nPlaylist '{nome_playlist}' criada com sucesso.")
            valid = True


        midias = songs_list + podcasts_list
        midias.append('Sair')
        valid = False
        
        while len(midias) != 1:
            print('\nEscolha uma música para adicionar:')
            

            Menu.enumarate_logic(midias, False)

            midias_len = len(midias)
            option = Menu.selection_logic(midias_len)

            if option == midias_len:
                break

            new_playlist.adicionar_midia(midias[option - 1])
            print(f'{midias[option - 1]} adicionada com sucesso')
            midias.pop(option - 1)
            
    def concatenar_playlists(user):
        playlists = list(user.playlists)

        playlists_copy = playlists.copy()


        playlists_len = len(playlists_copy)

        if len(playlists_copy) < 2:
            print('\nQuantidade de playlists insuficientes para realizar essa ação')
            print(f'Atulamente existem {playlists_len} playlist(s)')
            return

        Menu.enumarate_logic(playlists_copy)
        option = Menu.selection_logic(playlists_len)

        playlist_1 = playlists_copy[option - 1]

        playlists_copy.remove(playlist_1)

        Menu.enumarate_logic(playlists_copy)
        option2 = Menu.selection_logic(playlists_len - 1)

        playlist_2 = playlists_copy[option2 - 1]

        p_new = user.concatenar_playlists(playlist_1,playlist_2)

        print('Playlists Concatenadas com sucesso')

    @staticmethod
    def gerar_relatorio(users_list, songs_list, playlists_list):
        """Gera um relatório com análises e salva em relatorios/relatorio.txt"""

        try:
            top_musicas_reproduzidas = Analises.top_musicas_reproduzidas(songs_list, 5)
            playlist_mais_popular = Analises.playlist_mais_popular(playlists_list)
            usuario_mais_ativo = Analises.usuario_mais_ativo(users_list)
            media_avaliacoes = Analises.media_avaliacoes(songs_list)
            total_reproducoes = Analises.total_reproducoes(users_list)


            relatorio = []
            relatorio.append("===== RELATÓRIO DO SISTEMA DE STREAMING =====\n")
            relatorio.append(f"Total de usuários: {len(users_list)}\n")

            relatorio.append(f"Top musicas reproduzidas: {top_musicas_reproduzidas}\n")
            relatorio.append(f"Playlist mais popular: {playlist_mais_popular}\n")
            relatorio.append(f"Média das avaliações das músicas: {media_avaliacoes}\n")
            relatorio.append(f"Total de reproducoes: {total_reproducoes}\n")
            relatorio.append(f"Usuário mais ativo: {usuario_mais_ativo}\n")
            relatorio.append("=============================================\n")

            relatorio_path = Path(__file__).parent / "relatorios/relatorio.txt"

        
            with open(relatorio_path, "w", encoding="utf-8") as file:
                file.writelines(relatorio)

            print(f"\nRelatório gerado com sucesso!")

        except Exception as e:
            LeArquivo.log_error(e, "Erro ao gerar relatório")
            print("Ocorreu um erro ao gerar o relatório.")

    def enumarate_logic(options: list, print_select=True):
        if print_select:
            print(f"\nSelecione uma das opções:")
        print()
        for idx, o in enumerate(options):
            print(f"<{idx + 1}> - {o}")

    def selection_logic(n_options):
        option = 0
        valid = False
        while (not valid):
            try:
                option = int(input("\nEscolha sua opção: "))
                if (option >= 1 and option <= n_options):
                    valid = True
                else:
                    print(f"Opção inválida. Escolha entre 1 e {n_options}")
            except ValueError:
                print("Opção inválida. Tente novamente.")

        return option
    
    def create_new_user(users_list):
        print("Criar novo usuário")
        valid = False
        while not valid:
            nome_usuario = input("Digite o nome do usuário: ")
            usuario_existente = any(u.nome == nome_usuario for u in users_list) 
            try:
                if usuario_existente:
                    print(f"Erro: O nome de usuário '{nome_usuario}' já existe.\n")
                    raise Exception(f'O nome de usuário {nome_usuario} já existe')
                else:
                    new_user = Usuario(nome_usuario, [])
                    users_list.append(new_user)
                    print(f"Usuário '{new_user.nome}' criado com sucesso.")
                    valid = True
            except Exception as e:
                LeArquivo.log_error(e, f"Usuário '{nome_usuario}' já existe")

    def avaliar_musica(user, songs_list):
        print('\nEscolha uma música para avaliar:')
        Menu.enumarate_logic(songs_list, False)

        songs_len = len(songs_list)
        option = Menu.selection_logic(songs_len)

        musica = songs_list[option - 1]

        nota = -1
        while nota < 1 or nota > 5:
            try:
                nota = int(input('\nEscolha uma nota de 1 a 5: '))
                if nota < 1 or nota > 5:
                    raise ValueError("Avaliação inválida)")
                break  
            except ValueError as e:
                print("\nErro: digite um número inteiro entre 1 e 5.")
                LeArquivo.log_error(e, "(nota fora do intervalo)")

        musica.avaliar(nota)
        print(f'\n{musica.titulo} avaliada com a nota {nota} com sucesso!')




    def create_match_playlist_option(u1: Usuario, users_list):
        print("\nCriar match")
        print("Escolha o usuário para fazer o match")

        opcoes = [u for u in users_list if u.nome != u1.nome]

        for idx, u in enumerate(opcoes):
            print(f"<{idx+1}> - {u.nome}")
        
        users_len = len(opcoes)
        op = Menu.selection_logic(users_len) -1
        u2 = opcoes[op]
        
        new_playlist = Analises.create_match_playlists(u1, u2)

        if new_playlist:
            u1.playlists.append(new_playlist)
            print(f"Playlis '{new_playlist.nome}' criada e adicionada a sua biblioteca")
        else:
            print("Não foi possivel criar a playlist.")