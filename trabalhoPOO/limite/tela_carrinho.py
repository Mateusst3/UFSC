class TelaCarrinho:

    def opcoes(self):
        print('---------------------------------Opções---------------------------------')

    def mostra_restaurantes_produtos(self, string):
        print(string)

    def escolhe_restaurante(self):
        resposta = int(input('De qual restaurante você deseja adicionar o produto? '))
        return resposta
