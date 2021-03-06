from limite.tela_menu import TelaMenu
from controle.controlador_restaurante import ControladorRestaurante


class ControladorMenu:

    def __init__(self, controlador_sistema):
        self.__tela_menu = TelaMenu()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_restaurante = ControladorRestaurante(self)

    def abrir_menu(self):
        self.abrir_tela()

    def fecha_sistema(self):
        exit(0)

    def cadastrar_restaurante(self):
        self.__controlador_restaurante.cadastro_restaurante()

    def lista_restaurantes(self):
        self.__controlador_restaurante.lista_restaurantes()

    def exclui_restaurante(self):
        self.__controlador_restaurante.exclui_restaurante()

    def altera_restaurante(self):
        self.__controlador_restaurante.altera_nome_restaurante()

    def cadastra_produto(self):
        self.__controlador_restaurante.adiciona_produto()

    def lista_produtos(self):
        self.__controlador_restaurante.lista_produtos_restaurantes()

    def adiciona_carrinho(self):
        self.__controlador_restaurante.adiciona_produto_carrinho()

    def fechar_compra(self):
        self.__controlador_restaurante.fechar_compra()

    def abrir_tela(self):
        opcoes_sistema = {1: self.cadastrar_restaurante, 2: self.exclui_restaurante,
                          3: self.altera_restaurante, 4: self.lista_restaurantes,
                          5: self.cadastra_produto, 6: self.lista_produtos, 7: self.adiciona_carrinho,
                          8: self.fechar_compra, 9: self.fecha_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_menu.inicia_menu()
            funcao_escolhida = opcoes_sistema[opcao_escolhida]
            funcao_escolhida()
