class Contratante:
    def __init__(self, nome, endereco, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        uuidParam = uuid.uuid1().int
        self.__id = int(str(uuidParam)[:6])

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_telefone(self):
        return self.__telefone

    def get_endereco(self):
        return self.__endereco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_id(self):
        return self.__id