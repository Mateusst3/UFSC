class TelaRestaurantes:

    def cadastra_restaurante(self):
        print('-----------Cadastra Restaurante-------------')
        restaurante = str(input('Qual o nome do restaurante que você deseja cadastrar? '))
        return restaurante

    def lista_restaurantes(self, restaurantes):
        if(len(restaurantes) > 0 ):
            print(restaurantes)
        else:
            print("Nenhum restaurante cadastrado")