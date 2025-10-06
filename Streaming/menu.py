from Streaming.usuario import Usuario

class Menu:
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

        return users_teste[Menu.selection_logic(users_len) - 1]

    def user_options(usuario):
        print(f"\nSelecione uma das opções:")
        print(f"<1> - Reproduzir uma música")
        print(f"<2> - Listar músicas")
        print(f"<3> - Listar playlists")
        print(f"<4> - Reproduzir uma playlist")
        print(f"<5> - Listar playlists")
        print(f"<6> - Criar nova playlist")
        print(f"<7> - Concatenar playlists")
        print(f"<8> - Gerar relatório")
        print(f"<9> - Sair")

        option = Menu.selection_logic(9)
        print(usuario)
        match (option):
            case 1: print('a')
            case 2: print('b')
            case 3: print('c')
            case 4: print('d')
            case 5: print('e')
            case 6: print('f')
            case 7: print('g')
            case 8: print('h')
            case _: option = 9

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
