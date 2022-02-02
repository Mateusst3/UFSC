from entidade.entidade_carrinho import Carrinho
from limite.tela_carrinho import TelaCarrinho

class ControladorCarrinho:

    def __init__(self, controlador_carrinho):
        self.__controlador_carrinho = controlador_carrinho
        self.__carrinho = Carrinho()
        self.__tela_carrinho = TelaCarrinho

    def adiciona_produto(self, restaurantes):
        self.__tela_carrinho.opcoes()
        x = 1
        for restaurante in restaurantes:
            self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(x) + '] ' + restaurante.get_nome())
            for produto in restaurante.get_produtos():
                self.__tela_carrinho.mostra_restaurantes_produtos(self,'     - produto: ' + produto.get_nome() +
                                                    ' , preço: ' + str(produto.get_preco()))
            x += 1
        opcao = self.__tela_carrinho.escolhe_restaurante()
        print(restaurantes[opcao].get_nome())
