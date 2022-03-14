from entidade.entidade_carrinho import Carrinho
from limite.tela_carrinho import TelaCarrinho
from entidade.entidade_compra_finalizada import CompraFinalizada


class ControladorCarrinho:

    def __init__(self, controlador_carrinho):
        self.__controlador_carrinho = controlador_carrinho
        self.__carrinho = Carrinho()
        self.__tela_carrinho = TelaCarrinho
        self.__compra_finalizada = CompraFinalizada
        self.__lista_compras_finalizadas = []

    def adiciona_produto(self, restaurantes):
        global nome_restaurante
        tem_produto = self.verifica_existe_produto(restaurantes)
        if tem_produto:
            nome_restaurantes = []
            for restaurante in restaurantes:
                nome_restaurantes.append(restaurante.get_nome()[0])
            button, nome_restaurante = self.__tela_carrinho.escolhe_exclui_mostra_restaurante_produto(self,
                                                                                                      'De qual restaurante você vai '
                                                                                                      'querer adicionar um produto?',
                                                                                                      nome_restaurantes,
                                                                                                      'Ok, selecionar restaurante')
            if 'Cancelar' in button:
                return
            else:
                for restaurante in restaurantes:
                    if restaurante.get_nome()[0] == nome_restaurante[0][0]:
                        lista_produtos = []
                        for _produto in restaurante.get_produtos():
                            lista_produtos.append(_produto.get_nome())
                        button, produto = self.__tela_carrinho.escolhe_exclui_mostra_restaurante_produto(self,
                                                                                                         'Qual produto você quer adicionar ao '
                                                                                                         'carrinho?',
                                                                                                         lista_produtos,
                                                                                                         'Ok, adicionar produto'
                                                                                                         )
                        for produtos in restaurante.get_produtos():
                            if produtos.get_nome() == produto[0][0]:
                                self.__carrinho.append_lista(produtos)
                                self.__tela_carrinho.sucesso(self, produtos)
        else:
            self.__tela_carrinho.mostra_exception(self, 'Você deve cadastar um produto primeiro!')

    def adiciona_ao_carrinho(self, restaurantes):
        adicionando = True
        while adicionando:
            opcao = self.__tela_carrinho.opcoes_inicial(self)
            if opcao == 1:
                self.adiciona_produto(restaurantes)
            if opcao == 2:
                self.remove_produto()
            if opcao == 4:
                self.ver_compras_finalizadas()
            else:
                adicionando = False

        return self.__carrinho.mostra_lista()

    def remove_produto(self):
        if len(self.__carrinho.mostra_lista()) > 0:
            nome_produto = []
            for produto in self.__carrinho.mostra_lista():
                nome_produto.append(produto.get_nome())
            button, a_remover = self.__tela_carrinho.escolhe_exclui_mostra_restaurante_produto(self,
                                                                                               'Qual produto você quer remover?',
                                                                                               nome_produto,
                                                                                               'Remover produto selecionado')
            if 'Cancelar' in button:
                return

            else:
                for produto_excluir in self.__carrinho.mostra_lista():
                    if produto_excluir.get_nome() == a_remover[0][0]:
                        self.__carrinho.mostra_lista().remove(produto_excluir)
        else:
            self.__tela_carrinho.mostra_exception(self, 'Você não tem nenhum produto no carrinho')

    def fechar_compra(self, carrinho):
        if len(carrinho) > 0:
            lista_produtos_nomes = []
            for produto in carrinho:
                lista_produtos_nomes.append('Produto: ' + produto.get_nome() + ', preço: R$' + str(produto.get_preco()))
            self.__tela_carrinho.escolhe_exclui_mostra_restaurante_produto(self, 'Resumo das compras',
                                                                           lista_produtos_nomes, 'Ok')
            fechar_compra = self.__tela_carrinho.fechar_compra(self)
            if fechar_compra == 1:
                self.pagar(carrinho)
            else:
                return carrinho
        else:
            self.__tela_carrinho.mostra_exception(self, 'Você deve cadastar um produto primeiro!')
            return carrinho

    def pagar(self, carrinho):
        preco_final = []
        for produto in carrinho:
            preco_final.append(produto.get_preco())
        preco_somado = sum(preco_final)
        forma_pagamento = self.__tela_carrinho.pagamento(self, preco_somado)
        if forma_pagamento == 1:
            cartao = 'crédito'
        if forma_pagamento == 2:
            cartao = 'débito'
        self.passar_cartao(cartao, carrinho)

    def passar_cartao(self, forma_pagamento, carrinho):
        self.__tela_carrinho.passar_cartao(self, forma_pagamento)
        self.__tela_carrinho.sucesso_pagamento(self)
        self.__compra_finalizada = CompraFinalizada(carrinho)
        self.__lista_compras_finalizadas.append(self.__compra_finalizada)
        self.limpa_carrinho()
        return self.__carrinho.mostra_lista()

    def verifica_existe_produto(self, restaurantes):
        restaurantes_sem_produto = []
        for restaurante in restaurantes:
            if len(restaurante.get_produtos()) == 0:
                restaurantes_sem_produto.append(restaurante)
        if len(restaurantes_sem_produto) == len(restaurantes):
            return False
        else:
            return True

    def ver_compras_finalizadas(self):
        if len(self.__lista_compras_finalizadas) >= 1:
            compras = []
            for compra_fechada in self.__lista_compras_finalizadas:
                produtos = ', '.join(compra_fechada.get_nome_produtos())
                preco = sum(compra_fechada.get_preco_produtos())
                compra_finalizada = ''.join('Produtos comprados: ' + produtos + ', preço: R$' + str(preco))
                compras.append(compra_finalizada)
            self.__tela_carrinho.mostra_compra_fechada(self, compras)
        else:
            self.__tela_carrinho.mostra_exception(self, 'Você não fez nenhuma compra!')

    def limpa_carrinho(self):
        self.__carrinho.exclui_lista()
