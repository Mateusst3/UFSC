class TelaCarrinho:

    def opcoes(self):
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

    def opcoes_final(self):
        print('O que você deseja fazer agora?')
        print('[1] Adicionar um produto ao carrinho')
        print('[2] Voltar ao sistema?')
        resposta = int(input('Escolha: '))
        return resposta
