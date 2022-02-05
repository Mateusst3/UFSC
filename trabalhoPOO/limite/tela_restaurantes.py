class TelaRestaurantes:

    def cadastra_restaurante(self):
        print('-----------Cadastra Restaurante-------------')
        restaurante = str(input('Qual o nome do restaurante que você deseja cadastrar? '))
        return restaurante

    def lista_restaurantes(self, restaurante):
        print(restaurante)

    def sem_restaurante_cadastrado(self):
        print('nenhum restaurante cadastrado')

    def exclui_restaurante(self):
        resposta = int(input('Qual restaurante você deseja excluir? '))
        return resposta

    def altera_nome_restaurante(self):
        resposta = int(input('Qual restaurante você deseja alterar o nome? '))
        return resposta

    def novo_nome(self):
        resposta = str(input('Qual o novo nome do restaurante? '))
        return resposta

    def adiciona_produto_restaurante(self):
        resposta = int(input('Para qual restaurante você deseja adicionar o produto? '))
        return resposta
