class Carrinho:

    def __init__(self):
        self.__nome = 'carrinho'
        self.__lista_compras = []

    def append_lista(self, Produto):
        self.__lista_compras.append(Produto)

    def mostra_lista(self):
        return self.__lista_compras