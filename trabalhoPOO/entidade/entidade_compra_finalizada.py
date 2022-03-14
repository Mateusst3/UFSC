class CompraFinalizada:

    def __init__(self, lista_produto):
        self.__lista_produtos_comprados = lista_produto

    def get_nome_produtos(self):
        lista_nome_produtos = []
        for produto in self.__lista_produtos_comprados:
            lista_nome_produtos.append(produto.get_nome())
        return lista_nome_produtos

    def get_preco_produtos(self):
        lista_preco_produtos = []
        for produto in self.__lista_produtos_comprados:
            lista_preco_produtos.append(produto.get_preco())
        return lista_preco_produtos
