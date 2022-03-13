class Restaurante:

    def __init__(self, nome):
        self.__nome = nome
        self.__produtos = []

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def adiciona_produto(self, produto):
        self.__produtos.append(produto)

    def get_produtos(self):
        return self.__produtos
