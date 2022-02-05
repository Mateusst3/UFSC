from entidade.entidade_restaurante import Restaurante
from limite.tela_restaurantes import TelaRestaurantes
from entidade.entidade_produto import Produto
from limite.tela_produtos import TelaProdutos
from controle.controlador_carrinho import ControladorCarrinho


class ControladorRestaurante:

    def __init__(self, controlador_restaurante):
        self.__tela_restaurante = TelaRestaurantes
        self.__restaurantes = []
        self.__controlador_restaurante = controlador_restaurante
        self.__tela_produtos = TelaProdutos
        self.__carrinho_controlador = ControladorCarrinho(self)
        self.__carrinho_fechado = []


    def cadastro_restaurante(self):
        nome_restaurante = self.__tela_restaurante.cadastra_restaurante(self)
        restaurante = Restaurante(nome_restaurante)
        self.__restaurantes.append(restaurante)

    def exclui_restaurante(self):
        self.lista_restaurantes()
        exclui = self.__tela_restaurante.exclui_restaurante(self)
        a_excluir = self.__restaurantes[exclui - 1]
        self.__restaurantes.remove(a_excluir)

    def adiciona_produto(self):
        self.lista_restaurantes()
        restaurante_adiciona = self.__tela_restaurante.adiciona_produto_restaurante(self)
        nome_produto = self.__tela_produtos.nome_produto(self)
        preco_produto = self.__tela_produtos.preco_produto(self, nome_produto)
        produto = Produto(nome_produto, preco_produto)
        self.__restaurantes[restaurante_adiciona - 1].adiciona_produto(produto)

    def lista_produtos_restaurantes(self):
        x = 1
        for restaurante in self.__restaurantes:
            self.__tela_restaurante.lista_restaurantes(self, '[' + str(x) + '] ' + restaurante.get_nome())
            for produto in restaurante.get_produtos():
                self.__tela_produtos.mostra_produto(self,'     - produto: ' + produto.get_nome() +
                                                    ' , preço: ' + str(produto.get_preco()))
            x += 1

    def lista_restaurantes(self):
        if len(self.__restaurantes) > 0:
            y = 1
            for restaurante in self.__restaurantes:
                self.__tela_restaurante.lista_restaurantes(self, '[' + str(y) + ']' + ' ' + restaurante.get_nome())
                y += 1

        else:
            self.__tela_restaurante.sem_restaurante_cadastrado()

    def adiciona_produto_carrinho(self):
        self.__carrinho_fechado = self.__carrinho_controlador.adiciona_ao_carrinho(self.__restaurantes)

    def fechar_compra(self):
        self.__carrinho_controlador.fechar_compra(self.__carrinho_fechado)
