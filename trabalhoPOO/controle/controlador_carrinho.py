from entidade.entidade_carrinho import Carrinho
from limite.tela_carrinho import TelaCarrinho


class ControladorCarrinho:

    def __init__(self, controlador_carrinho):
        self.__controlador_carrinho = controlador_carrinho
        self.__carrinho = Carrinho()
        self.__tela_carrinho = TelaCarrinho

    def adiciona_produto(self, restaurantes):
        self.__tela_carrinho.opcoes(self)
        x = 1
        for restaurante in restaurantes:
            self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(x) + '] ' + restaurante.get_nome())
            for produto in restaurante.get_produtos():
                self.__tela_carrinho.mostra_restaurantes_produtos(self, '     - produto: ' + produto.get_nome() +
                                                                  ' , preço: ' + str(produto.get_preco()))
            x += 1
        opcao = self.__tela_carrinho.escolhe_restaurante(self)
        self.__tela_carrinho.opcoes(self)
        produtos_restaurante_escolhido = restaurantes[opcao - 1].get_produtos()
        y = 1
        for produto in produtos_restaurante_escolhido:
            self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(y) + ']' + 'produto: ' +
                                                              produto.get_nome() + ', preço: ' +
                                                              str(produto.get_preco())
                                                              + 'R$')
        produto_inteiro = self.__tela_carrinho.escolhe_produto(self)
        produto_escolhido = produtos_restaurante_escolhido[produto_inteiro - 1]
        self.__carrinho.append_lista(produto_escolhido)
        self.__tela_carrinho.sucesso(self)

    def adiciona_ao_carrinho(self, restaurantes):
        adicionando = True
        while adicionando:
            opcao = self.__tela_carrinho.opcoes_final(self)
            if opcao == 1:
                self.adiciona_produto(restaurantes)
            else:
                adicionando = False

        return self.__carrinho.mostra_lista()
