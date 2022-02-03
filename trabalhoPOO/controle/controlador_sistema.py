from limite.tela_sistema import TelaSistema
from controle.controlador_menu import ControladorMenu


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_menu = ControladorMenu(self)

    def inicializa_sistema(self):
        self.abrir_tela()

    def fechar_sistema(self):
        exit(0)

    def abre_menu(self):
        self.__controlador_menu.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.abre_menu, 2: self.fechar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_sistema()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
