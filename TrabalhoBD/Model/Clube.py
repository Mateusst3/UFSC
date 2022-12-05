import uuid


class Clube:

    def __init__(self, nome, endereco):
        self.__nome = nome
        uuidParam = uuid.uuid1().int
        self.__id = int(str(uuidParam)[:6])
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    def get_id(self):
        return self.__id
