class TelaMenu:

    def inicia_menu(self):
        print("----------Menu do sistema----------")
        print("O que você deseja fazer?")
        print("[1] Cadastrar restaurante")
        print("[2] Excluir restaurante")
        print("[3] Ver todos os restaurantes")
        print("[4] Cadastrar produtos")
        print("[5] Lista produtos")
        print("[6] Comprar produtos")
        print("[7] Fechar o sistema")
        print("-----------------------------------")
        opcoes = int(input("escolha: "))
        return opcoes
