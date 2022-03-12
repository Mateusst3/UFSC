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
        if len(self.__restaurantes) > 0:
            # self.lista_restaurantes()
            nome_restaurante = []
            y = 1
            for restaurante in self.__restaurantes:
                nome_restaurante.append(restaurante.get_nome()[0])
                y += 1
            button, nome_excluido = self.__tela_restaurante.exclui_altera_nome_adiciona(self,
                                                                                        'Qual restaurante você deseja '
                                                                                        'excluir?',
                                                                                        nome_restaurante, 'Excluir')
            if 'Cancelar' in button:
                pass
            else:
                for restaurante in self.__restaurantes:
                    if restaurante.get_nome()[0] == nome_excluido[0]:
                        self.__restaurantes.remove(restaurante)

            # a_excluir = self.__restaurantes[exclui - 1]
            # self.__restaurantes.remove(a_excluir)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def adiciona_produto(self):
        if len(self.__restaurantes) > 0:
            self.lista_restaurantes()
            restaurante_adiciona = self.__tela_restaurante.adiciona_produto_restaurante(self)
            nome_produto = self.__tela_produtos.nome_produto(self)
            preco_produto = self.__tela_produtos.preco_produto(self, nome_produto)
            produto = Produto(nome_produto, preco_produto)
            self.__restaurantes[restaurante_adiciona - 1].adiciona_produto(produto)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def altera_nome_restaurante(self):
        if len(self.__restaurantes) > 0:
            self.lista_restaurantes()
            altera = self.__tela_restaurante.altera_nome_restaurante(self)
            novo_nome = self.__tela_restaurante.novo_nome(self)
            self.__restaurantes[altera - 1].nome(novo_nome)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def lista_produtos_restaurantes(self):
        x = 1
        if len(self.__restaurantes) > 0:
            self.__tela_restaurante(self.__restaurantes)
            # for restaurante in self.__restaurantes:
            #     self.__tela_restaurante.lista_restaurantes(self, '[' + str(x) + '] ' + restaurante.get_nome())
            #     for produto in restaurante.get_produtos():
            #         self.__tela_produtos.mostra_produto(self, '     - produto: ' + produto.get_nome() +
            #                                             ' , preço: ' + str(produto.get_preco()))
            #     x += 1
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def lista_restaurantes(self):
        if len(self.__restaurantes) > 0:
            nome_restaurante = []
            y = 1
            for restaurante in self.__restaurantes:
                nome_restaurante.append(restaurante.get_nome()[0])
                y += 1
            self.__tela_restaurante.lista_restaurantes(self, nome_restaurante)

        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def adiciona_produto_carrinho(self):
        self.__carrinho_fechado = self.__carrinho_controlador.adiciona_ao_carrinho(self.__restaurantes)

    def fechar_compra(self):
        self.__carrinho_controlador.fechar_compra(self.__carrinho_fechado)
