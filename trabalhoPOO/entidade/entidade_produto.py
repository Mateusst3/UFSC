class Produto:

    def __init__(self, nome: str, preco: int):
        self.__nome = nome
        self.__preco = preco

    def nome(self, nome):
        self.__nome = nome

    def preco(self, preco):
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco
