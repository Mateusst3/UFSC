class TelaSistema:
    def tela_sistema(self):
        print("----------Sistema de Delivery----------")
        print("O que você deseja fazer?")
        print("[1] Entrar no sistema")
        print("[2] Fechar o sistema")
        print("---------------------------------------")
        opcao = int(input('Escolha: '))
        return opcao

    def mostra_exception(self, str):
        print(str)

    def excepiton_inicial(self, str):
        print(str)
        print('Opção inválida, reinicie o sistema!')