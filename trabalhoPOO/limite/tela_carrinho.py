class TelaCarrinho:

    def opcoes__(self):
        print('---------------------------------Opções---------------------------------')

    def mostra_restaurantes_produtos(self, string):
        print(string)

    def escolhe_restaurante(self):
        resposta = int(input('De qual restaurante você deseja adicionar o produto? '))
        return resposta

    def escolhe_produto(self):
        resposta = int(input('Qual produto você deseja comprar? '))
        return resposta

    def sucesso(self):
        print('Produto adicionado com sucesso!')

    def opcoes_inicial(self):
        print('O que você deseja fazer agora?')
        print('[1] Adicionar um produto ao carrinho')
        print('[2] Voltar ao sistema?')
        resposta = int(input('Escolha: '))
        return resposta

    def carrinho__(self):
        print('---------------------------------Produtos no seu carrinho---------------------------------')

    def fechar_compra(self):
        print('Você deseja finalizar sua compra? ')
        print('[1] Sim')
        print('[2] Não')
        resposta = int(input('Resposta: '))
        return resposta

    def pagamento(self, preco):
        print('O total de suas compras deu: ' + str(preco) + 'R$')
        print('Qual sua forma de pagamento?')
        print('[1] Cartão de crédito')
        print('[2] Cartão de débito')
        resposta = int(input('Escolha: '))
        return resposta

    def passar_cartao(self, forma_pagamento):
        int(input('digite o numero do seu cartão de ' + forma_pagamento + ': '))
        print('Operação finalizada com sucesso!')
        print('Você finalizou sua compra! O sistema será encerrado')
