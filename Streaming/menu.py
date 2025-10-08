from Streaming.usuario import Usuario
from Streaming.analises import Analises

class Menu:
    users = []
    def initialize():
        option = 0

        while (option != 4):
            option = Menu.select_option()
            match (option):
                case 1: Menu.user_options(Menu.sign_in_user())
                case 2: print('b') 
                case 3: print('c')
                case _: option = 4

        print("Fim do programa!")

    def select_option() -> int:
        print(f"\nSelecione uma das opções:")
        print(f"<1> - Entrar como usuário")
        print(f"<2> - Criar novo usuário")
        print(f"<3> - Listar usuários")
        print(f"<4> - Finalizar programa")

        return Menu.selection_logic(4)

    def sign_in_user():
        users_teste = ['u1', 'u2', 'u3']  # lista de usuarios
        for idx, u in enumerate(users_teste):
            print(f"<{idx + 1}> - {u}")

        users_len = len(users_teste)

        option = Menu.selection_logic(users_len) - 1
    # print()

        return users_teste[option]

    def user_options(usuario):
        print(f"\nSelecione uma das opções:")
        print(f"<1> - Reproduzir uma música")
        print(f"<2> - Listar músicas")
        print(f"<3> - Listar playlists")
        print(f"<4> - Reproduzir uma playlist")
        print(f"<5> - Criar nova playlist")
        print(f"<6> - Concatenar playlists")
        print(f"<7> - Gerar relatório")
        print(f"<8> - Criar match")
        print(f"<9> - Sair")

        option = 0

        print(usuario)
        while (option != 9):
            option = Menu.selection_logic(9)
            match (option):
                case 1: Menu.reproduzir_musica(usuario)
                case 2: Menu.create_new_user()
                case 3: print('c')
                case 4: print('d')
                case 5: print('e')
                case 6: print('f')
                case 7: print('g')
                case 8: print (Menu.create_match_playlist_option(usuario))
                case _: option = 9

    def reproduzir_musica(user):
        # musicas = user.musicas
        musicas_teste = ['mus1', 'mus2', 'mus3']  # lista de musicas usuarios

        for idx, u in enumerate(musicas_teste):
            print(f"<{idx + 1}> - {u}")
        
        musicas_len = len(musicas_teste)
        option = Menu.selection_logic(musicas_len)

        Usuario.ouvir_midia(musicas_teste[option - 1])
        

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
    def create_new_user():
        print("Criar novo usuário")
        while True:
            nome_usuario = input("Digite o nome do usuário: ")
            usuario_existente = any(u.nome == nome_usuario for u in Menu.users) 
            if usuario_existente:
                print(f"Erro.: O nome de usuário '{nome_usuario}' já existe.")
            else:
                new_user = Usuario(nome=nome_usuario, playlists=[])
                Menu.users.append(new_user)
                print(f"Usuário '{new_user.nome}' criado com sucesso.")

    def create_match_playlist_option(u1: Usuario):
        print("Criar match")
        print("Escolha o usuário para fazer o match")

        opcoes = [u for u in Menu.all_usuers if u.nome != u1.nome]

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