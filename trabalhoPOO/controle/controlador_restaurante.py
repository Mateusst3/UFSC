from entidade.entidade_restaurante import Restaurante
from limite.tela_restaurantes import TelaRestaurantes


class ControladorRestaurante:

    def __init__(self, controlador_restaurante):
        self.__tela_restaurante = TelaRestaurantes
        self.__restaurantes = []
        # self.__restaurante = Restaurante
        self.__controlador_restaurante = controlador_restaurante


    def cadastro_restaurante(self):
        nome_restaurante = self.__tela_restaurante.cadastra_restaurante(self)
        restaurante = Restaurante(nome_restaurante)
        self.__restaurantes.append(restaurante)


    def lista_restaurantes(self):
        self.__tela_restaurante.lista_restaurantes(self, self.__restaurantes)

