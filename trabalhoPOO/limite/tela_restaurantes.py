from limite.tela_pai import Tela
import PySimpleGUI as sg


class TelaRestaurantes(Tela):

    def __init__(self):
        self.__window = None

    def mostra_exception(self, exception):
        sg.Popup('Tivemos o seguinte problema: ' + exception)

    def cadastra_restaurante(self):
        layout = [
            [sg.Text('')],
            [sg.Text('Nome do restaurante', size=(15, 1)), sg.InputText()],
            [sg.Submit('Cadastrar')]
        ]

        self.__window = sg.Window('Cadastrar novo restaurante', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return values

    def troca_nome(self):
        layout = [
            [sg.Text('Novo nome restaurante', size=(15, 1)), sg.InputText()],
            [sg.Submit('Cadastrar novo nome')]
        ]
        self.__window = sg.Window('Alterar nome').Layout(layout)
        values = self.__window.Read()
        self.__window.Close()
        return values

    def lista_restaurantes(self, restaurantes):
        layout = [
            [sg.Text('Estes são os restaurantes cadastrados')],
            [sg.Combo(restaurantes, ['restaurantes....'])],
            [sg.Button('Ok, fechar janela')],
        ]
        self.__window = sg.Window('Restaurantes cadastrados', default_element_size=(500, 1)).Layout(layout)
        self.__window.Read()
        self.__window.Close()

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

    def exclui_altera_nome_adiciona(self, texto_input, lista, action):
        layout = [
            [sg.Text(texto_input)],
            [sg.Combo(lista)],
            [sg.Button(action), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('', default_element_size=(500, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
