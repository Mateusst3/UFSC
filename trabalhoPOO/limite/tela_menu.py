class TelaMenu:

    def inicia_menu(self):
        print("----------Menu do sistema----------")
        print("O que você deseja fazer?")
        print("[1] Cadastrar restaurante")
        print("[2] Excluir restaurante")
        print("[3] Alterar nome do restaurante")
        print("[4] Ver todos os restaurantes")
        print("[5] Cadastrar produtos")
        print("[6] Lista produtos")
        print("[7] Comprar produtos")
        print("[8] Fechar compra")
        print("[9] Fechar o sistema")
        print("-----------------------------------")
        opcoes = int(input("escolha: "))
        return opcoes
