class TelaMenu:

    def inicia_menu(self):
        print("----------Menu do sistema----------")
        print("O que você deseja fazer?")
        print("[1] Cadastrar restaurante")
        print("[2] Ver todos os restaurantes")
        print("[3] Fechar o sistema")
        print("-----------------------------------")
        opcoes = int(input("escolha: "))
        return opcoes