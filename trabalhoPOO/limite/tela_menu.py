import PySimpleGUI as sg


class TelaMenu:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Menu do sistema, o que você deseja fazer?')],
            [sg.Button('Cadastrar restaurante', key='1')],
            [sg.Button('Excluir restaurante', key='2')],
            [sg.Button('Alterar nome do restaurante', key='3')],
            [sg.Button('Ver todos os restaurantes', key='4')],
            [sg.Button('Cadastrar produtos', key='5')],
            [sg.Button('Lista produtos', key='6')],
            [sg.Button('Comprar produtos', key='7')],
            [sg.Button('Fechar compra', key='8')],
            [sg.Button('Fechar o sistema', key='9')],
        ]
        self.__window = sg.Window('Menu do sistema', default_element_size=(40, 1)).Layout(layout)

    def inicia_menu(self):
        button, values = self.__window.Read()
        return int(button)