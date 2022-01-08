class Restaurante:

    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []


    def nome(self, nome: str):
        self.__nome = nome

    def adiciona_produto(self, Produto):
        self.__produtos.append(Produto)