class TelaProdutos:

    def nome_produto(self):
        resposta = str(input('Qual o nome do produto que você deseja adicionar? '))
        return resposta

    def preco_produto(self, nome_item):
        resposta = int(input('Qual o preço do item ' + nome_item + '? '))
        return resposta

    def mostra_produto(self, produto_formatado):
        print(produto_formatado)