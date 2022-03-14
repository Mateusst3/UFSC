import PySimpleGUI as sg
from limite.tela_pai import Tela


class TelaCarrinho(Tela):

    def mostra_exception(self, exception):
        sg.Popup('Tivemos o seguinte problema: ' + exception)

    def __init__(self):
        self.__window = None

    def escolhe_exclui_mostra_restaurante_produto(self, texto_inicial, lista, tipo_restaurante_produto):
        layout = [
            [sg.Text(texto_inicial)],
            [sg.Listbox(lista, size=(100, len(lista)))],
            [sg.Submit(tipo_restaurante_produto), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Lista de produtos').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def sucesso(self, produto):
        sg.Popup('Produto adicionado com sucesso!' + ' Produto: ' + produto.get_nome() + ', preço: R$' +
                 str(produto.get_preco()))

    def sucesso_pagamento(self):
        sg.Popup('Pagamento realizado com sucesso! Sua conta foi registrada')

    def opcoes_inicial(self):
        layout = [
            [sg.Text('O que você deseja fazer?')],
            [sg.Button('Adicionar um produto ao carrinho', key=1)],
            [sg.Button('Remover produto do carrinho', key=2)],
            [sg.Button('Voltar ao sistema', key=3)],
            [sg.Button('Ver compras finalizadas', key=4)]
        ]
        self.__window = sg.Window('Menu do sistema', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return int(button)

    def fechar_compra(self):
        layout = [
            [sg.Text('Você deseja finalizar sua compra?')],
            [sg.Button('Sim', key=1)],
            [sg.Button('Não', key=2)],
        ]
        self.__window = sg.Window('Fechar compra', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return int(button)

    def pagamento(self, preco):
        layout = [
            [sg.Text('O total de suas compras deu: R$' + str(preco))],
            [sg.Button('Cartão de crédito', key=1)],
            [sg.Button('Cartão de débito', key=2)],
        ]
        self.__window = sg.Window('Menu do sistema', default_element_size=(40, 1)).Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()
        return int(button)

    def passar_cartao(self, forma_pagamento):
        layout = [
            [sg.Text('Processar pagamento')],
            [sg.Text('Digite o número do cartão de ' + forma_pagamento), sg.InputText()],
            [sg.Submit('Pagar')]
        ]
        self.__window = sg.Window('Cadastrar novo restaurante', default_element_size=(40, 1)).Layout(layout)
        self.__window.Read()
        self.__window.Close()

    def mostra_compra_fechada(self, lista):
        layout = [
            [sg.Text('Lista de compras fechadas')],
            [sg.Listbox(lista, size=100)],
            [sg.Submit('Ok, voltar ao sistema')],
        ]
        self.__window = sg.Window('Lista de produtos').Layout(layout)
        self.__window.Read()
        self.__window.Close()
        return
