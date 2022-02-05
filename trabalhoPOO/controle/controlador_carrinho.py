from entidade.entidade_carrinho import Carrinho
from limite.tela_carrinho import TelaCarrinho


class ControladorCarrinho:

    def __init__(self, controlador_carrinho):
        self.__controlador_carrinho = controlador_carrinho
        self.__carrinho = Carrinho()
        self.__tela_carrinho = TelaCarrinho

    def adiciona_produto(self, restaurantes):
        tem_produto = self.verifica_existe_produto(restaurantes)
        if tem_produto:
            self.__tela_carrinho.opcoes__(self)
            x = 1
            for restaurante in restaurantes:
                self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(x) + '] ' + restaurante.get_nome())
                for produto in restaurante.get_produtos():
                    self.__tela_carrinho.mostra_restaurantes_produtos(self, '     - produto: ' + produto.get_nome() +
                                                                  ' , preço: ' + str(produto.get_preco()))
                x += 1
            opcao = self.__tela_carrinho.escolhe_restaurante(self)
            self.__tela_carrinho.opcoes__(self)
            produtos_restaurante_escolhido = restaurantes[opcao - 1].get_produtos()
            y = 1
            if len(produtos_restaurante_escolhido) > 0:
                for produto in produtos_restaurante_escolhido:
                    self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(y) + ']' + 'produto: ' +
                                                                      produto.get_nome() + ', preço: ' +
                                                                      str(produto.get_preco())
                                                                      + 'R$')
                    y += 1
                produto_inteiro = self.__tela_carrinho.escolhe_produto(self)
                produto_escolhido = produtos_restaurante_escolhido[produto_inteiro - 1]
                self.__carrinho.append_lista(produto_escolhido)
                self.__tela_carrinho.sucesso(self)
            else:
                self.__tela_carrinho.restaurante_sem_produtos(self)
        else:
            self.__tela_carrinho.sem_produtos(self)

    def adiciona_ao_carrinho(self, restaurantes):
        adicionando = True
        while adicionando:
            opcao = self.__tela_carrinho.opcoes_inicial(self)
            if opcao == 1:
                self.adiciona_produto(restaurantes)
            if opcao == 2:
                self.remove_produto()
            else:
                adicionando = False

        return self.__carrinho.mostra_lista()

    def remove_produto(self):
        if len(self.__carrinho.mostra_lista()) > 0:
            self.__tela_carrinho.carrinho__(self)
            y = 1
            for produto in self.__carrinho.mostra_lista():
                self.__tela_carrinho.mostra_restaurantes_produtos(self, '[' + str(y) + ']' + 'produto: ' +
                                                                  produto.get_nome() + ', preço: ' +
                                                                  str(produto.get_preco())
                                                                  + 'R$')
                y += 1
            produto_removido_int = self.__tela_carrinho.remove_produto(self)
            produto_removido = self.__carrinho.mostra_lista()[produto_removido_int - 1]
            self.__carrinho.mostra_lista().remove(produto_removido)
        else:
            self.__tela_carrinho.sem_produtos(self)

    def fechar_compra(self, carrinho):
        if len(carrinho) > 0:
            self.__tela_carrinho.carrinho__(self)
            for produto in carrinho:
                self.__tela_carrinho.mostra_restaurantes_produtos(self, 'produto: ' + produto.get_nome() + ' custa: '
                                                                  + str(produto.get_preco()) + 'R$')
            fechar_compra = self.__tela_carrinho.fechar_compra(self)
            if fechar_compra == 1:
                self.pagar(carrinho)
        else:
            self.__tela_carrinho.sem_produtos(self)

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
        self.passar_cartao(cartao)

    def passar_cartao(self, forma_pagamento):
        self.__tela_carrinho.passar_cartao(self, forma_pagamento)
        exit(0)

    def verifica_existe_produto(self, restaurantes):
        restaurantes_sem_produto = []
        for restaurante in restaurantes:
            if len(restaurante.get_produtos()) == 0:
                restaurantes_sem_produto.append(restaurante)
        if len(restaurantes_sem_produto) == len(restaurantes):
            return False
        else:
            return True
