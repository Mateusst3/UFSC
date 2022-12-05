import uuid


class Jogador:

    def __init__(self, nome):
        self.__nome = nome
        self.__id = uuid.uuid1().int

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id
