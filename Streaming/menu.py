from .usuario import Usuario
from .le_arquivo import LeArquivo
import os
from pathlib import Path


class Menu:
    def initialize():
        option = 0
        
        file_path = Path('TG1-POD/config/dados.md')
        

        users_list, songs_list, podcasts_list = LeArquivo.read_file(file_path)
        # print('users_list\n', users_list)

        # print('songs_list\n', songs_list)
        
        # print('podcasts_list\n', podcasts_list)



        while (option != 4):
            option = Menu.select__main_option()
            match (option):
                case 1: Menu.user_options(Menu.sign_in_user(users_list), songs_list, podcasts_list)
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

    def user_options(user, songs_list, podcasts_list):

        option = 0

        print(user)
        while (option != 8):
            option = Menu.select_user_option()
            match (option):
                case 1: Menu.reproduzir_musica(user)
                case 2: Menu.listar_musicas(user)
                case 3: Menu.listar_playlists(user)
                case 4: Menu.reproduzir_playlist(user)
                case 5: Menu.criar_nova_playlist(user, songs_list, podcasts_list)
                case 6: Menu.concatenar_playlists(user)
                case 7: Menu.gerar_relatorio(user)
                case _: option = 8

    def select_user_option():
        ls_options = ['Reproduzir uma música', 'Listar músicas', 'Listar playlists',
                      'Reproduzir uma playlist', 'Criar nova playlist',
                      'Concatenar playlists', 'Gerar relatório', 'Sair']
        Menu.enumarate_logic(ls_options)

        return Menu.selection_logic(8)

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

        playlists[option - 1].reproduzir()


    def criar_nova_playlist(user, songs_list, podcasts_list):

        valid = False
        while not valid:
            nome_playlist = input("Digite o nome da nova playlist: ")
            playlist_esiste = any(p.nome == nome_playlist for p in user.playlists) 
            if playlist_esiste:
                print(f"Erro: O nome de usuário '{nome_playlist}' já existe.\n")
                continue
            new_playlist = user.criar_playlist(nome_playlist)
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
            



        # Usuario.criar_playlist(nome)
        
    def create_new_user(users_list):
        print("Criar novo usuário")
        valid = False
        while not valid:
            nome_usuario = input("Digite o nome do usuário: ")
            usuario_existente = any(u.nome == nome_usuario for u in users_list) 
            if usuario_existente:
                print(f"Erro.: A playlist '{nome_usuario}' já existe.")
            else:
                new_user = Usuario(nome_usuario, [])
                users_list.append(new_user)
                print(f"Usuário '{new_user.nome}' criado com sucesso.")
                valid = True

    def concatenar_playlists(user):
        playlists = list(user.playlists)


        playlists_len = len(playlists)

        if len(playlists) < 2:
            print('\nQuantidade de playlists insuficientes para realizar essa ação')
            print(f'Atulamente existem {playlists_len} playlist(s)')
            return

        Menu.enumarate_logic(playlists)
        option = Menu.selection_logic(playlists_len)

        playlist_1 = playlists[option - 1]

        new_playlist_list = playlists.remove(playlist_1)

        Menu.enumarate_logic(playlists)
        option2 = Menu.selection_logic(playlists_len - 1)

        playlist_2 = playlists[option2 - 1]

        print('pl', playlist_1)
        print('p2', playlist_2)

        # p_new = playlist_1 + playlist_2

        # print(p_new)

    def gerar_relatorio(user):
        pass

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
