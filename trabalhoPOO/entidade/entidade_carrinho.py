class Carrinho:

    def __init__(self):
        self.__nome = 'carrinho'
        self.__lista_compras = []

    def append_lista(self, produto):
        self.__lista_compras.append(produto)

    def mostra_lista(self):
        return self.__lista_compras

    def exclui_lista(self):
        self.__lista_compras = []
