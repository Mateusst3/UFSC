from DBConf.DBConfig import DBConfig
from Model.QuadraEsportiva import QuadraEsportiva


class QuadraEsportivaService:

    dbConfig = DBConfig()

    def create_quadra(self, tipo_de_quadra, id_clube):
        quadra = QuadraEsportiva(tipo_de_quadra, id_clube)
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = "INSERT INTO Quadra_esportiva (id_quadra, tipo_de_quadra, id_clube) VALUES (%s, %s, %s)"
        values = (quadra.get_id(), quadra.get_tipo_de_quadra(), quadra.get_id_clube())
        cursor.execute(sql, values)
        db_connection.commit()
        return 'Quadra criada com sucesso na base de dados, dados: ' + 'id: ' + str(quadra.get_id())

    def exclude_quadra(self, id_quadra):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        values = str(id_quadra)
        sql = f"DELETE from Quadra_esportiva where id_quadra = '{values}'"
        cursor.execute(sql)
        db_connection.commit()
        return 'Quadra excluido com sucesso com id: ' + str(id_quadra)
