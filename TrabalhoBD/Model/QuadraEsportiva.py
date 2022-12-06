class QuadraEsportiva:
    def __init__(self, tipo_de_quadra, id_clube):
        self.__tipo_de_quadra = tipo_de_quadra
        uuidParam = uuid.uuid1().int
        self.__id = int(str(uuidParam)[:6])
        self.__id_clube = id_clube

    def get_tipo_de_quadra(self):
        return self.__tipo_de_quadra

    def set_tipo_de_quadra(self, tipo_de_quadra):
        self.__tipo_de_quadra = tipo_de_quadra

    def get_id_clube(self):
        return self.__tipo_de_quadra

    def set_id_clube(self, id_clube):
        self.__id_clube = id_clube

    def get_id(self):
        return self.__id
