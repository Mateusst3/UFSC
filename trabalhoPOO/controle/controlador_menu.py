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


    def abrir_tela(self):
        opcoes_sistema = {1: self.cadastrar_restaurante, 2: self.lista_restaurantes, 3: self.fecha_sistema}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_menu.inicia_menu()
            funcao_escolhida = opcoes_sistema[opcao_escolhida]
            funcao_escolhida()
