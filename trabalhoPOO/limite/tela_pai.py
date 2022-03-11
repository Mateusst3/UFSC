from abc import ABC, abstractmethod
import PySimpleGUI as sg


class Tela(ABC):

    @abstractmethod
    def mostra_exception(self, exception):
        pass
