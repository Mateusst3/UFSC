from abc import ABC, abstractmethod
import PySimpleGUI as sg


class Tela(ABC):

    @abstractmethod
    def mostra_exception(self, exception):
        sg.Popup('Alguma coisa deu errado! O sistema se desligará ' + exception)
