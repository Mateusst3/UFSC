import uuid


class Time:

    def __init__(self, nome):
        self.__nome = nome
        uuidParam = uuid.uuid1().int
        self.__id = int(str(uuidParam)[:6])

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id
