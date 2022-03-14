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
        for restaurante in self.__restaurantes:
            if restaurante.get_nome()[0] == nome_restaurante[0]:
                self.__tela_restaurante.mostra_exception(self, 'Já existe um restaurante com este nome!')
                return
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
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def adiciona_produto(self):
        if len(self.__restaurantes) > 0:
            nome_restaurante = []
            for restaurante in self.__restaurantes:
                nome_restaurante.append(restaurante.get_nome()[0])
            button, values = self.__tela_restaurante.exclui_altera_nome_adiciona(self, '', nome_restaurante,
                                                                                 'Quero adicionar um produto a este '
                                                                                 'restaurante')
            if 'Cancelar' in button:
                return
            else:
                butto, produto = self.__tela_restaurante.cadastra_produto(self, values[0])
                nome_produto = produto[0]
                preco_produto = int(produto[1])
                produto = Produto(nome_produto, preco_produto)
                for restaurante in self.__restaurantes:
                    if restaurante.get_nome()[0] == values[0]:
                        restaurante.adiciona_produto(produto)

            # self.lista_restaurantes()
            # restaurante_adiciona = self.__tela_restaurante.adiciona_produto_restaurante(self)
            # nome_produto = self.__tela_produtos.nome_produto(self)
            # preco_produto = self.__tela_produtos.preco_produto(self, nome_produto)
            # produto = Produto(nome_produto, preco_produto)
            # self.__restaurantes[restaurante_adiciona - 1].adiciona_produto(produto)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def altera_nome_restaurante(self):
        if len(self.__restaurantes) > 0:
            nome_restaurante = []
            for restaurante in self.__restaurantes:
                nome_restaurante.append(restaurante.get_nome()[0])
            button, value = self.__tela_restaurante.exclui_altera_nome_adiciona(self, '', nome_restaurante, 'Quero '
                                                                                                            'alterar '
                                                                                                            'este '
                                                                                                            'restaurante'
                                                                                                            '')
            button2, value_novo_nome = self.__tela_restaurante.troca_nome(self)
            if 'Cancelar' in button:
                return
            else:
                for restaurante in self.__restaurantes:
                    if restaurante.get_nome()[0] == value[0]:
                        print(value_novo_nome)
                        restaurante.set_nome(value_novo_nome)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def lista_produtos_restaurantes(self):
        if len(self.__restaurantes) > 0:
            lista_produtos_restaurante = []
            for restaurante in self.__restaurantes:
                for produto in restaurante.get_produtos():
                    lista_produtos_restaurante.append('Produto: ' + produto.get_nome() + ', com preço: ' +
                                                      str(produto.get_preco()) + ', do restaurante ' +
                                                      restaurante.get_nome()[0])
            self.__tela_restaurante.mostra_adiciona_produto_restaurante(self, lista_produtos_restaurante)
        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def lista_restaurantes(self):
        if len(self.__restaurantes) > 0:
            nome_restaurante = []
            for restaurante in self.__restaurantes:
                nome_restaurante.append(restaurante.get_nome()[0])
            self.__tela_restaurante.lista_restaurantes(self, nome_restaurante)

        else:
            self.__tela_restaurante.mostra_exception(self, 'Nenhum restaurante cadastrado!')

    def adiciona_produto_carrinho(self):
        self.__carrinho_fechado = self.__carrinho_controlador.adiciona_ao_carrinho(self.__restaurantes)

    def fechar_compra(self):
        self.__carrinho_controlador.fechar_compra(self.__carrinho_fechado)
