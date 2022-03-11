from limite.tela_sistema import TelaSistema
from controle.controlador_menu import ControladorMenu
from exceptions.exceptions import SpecialExceptions


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_menu = ControladorMenu(self)

    def inicializa_sistema(self):
        try:
            self.abrir_tela()

        except Exception as e:
            self.__tela_sistema.excepiton_inicial(e)

    def fechar_sistema(self):
        exit(0)

    def abre_menu(self):
        self.__controlador_menu.abrir_tela()

    def abrir_tela(self):
        lista_opcoes = {1: self.abre_menu, 2: self.fechar_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_sistema()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            # try:
            funcao_escolhida()
            # except Exception as exception:
            #     excepts = str(SpecialExceptions.captura_exception(str(exception)))
            #     self.__tela_sistema.mostra_exception(excepts)
