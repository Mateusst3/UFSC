import PySimpleGUI as sg
from limite.tela_pai import Tela


class TelaSistema(Tela):

    def mostra_exception(self, exception):
        sg.Popup('Alguma coisa deu errado! O sistema se desligará ' + exception)

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text('Entrar no sistema de delivery')],
            [sg.Button('Entrar'), sg.Cancel()],
        ]
        self.__window = sg.Window('Tela do sistema', default_element_size=(40, 1)).Layout(layout)

    def tela_sistema(self):
        button, values = self.__window.Read()
        self.__window.Close()
        return 1 if 'Entrar' in button else 2
