from DBConf.DBConfig import DBConfig
from Model.Time import Time


class TimeService:
    dbConfig = DBConfig()

    def create_jogador(self, nome_time):
        time = Time(nome_time)
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = "INSERT INTO Time (Nome, id_time) VALUES (%s, %s)"
        values = (time.get_nome(), time.get_id())
        cursor.execute(sql, values)
        db_connection.commit()
        return 'Time criado com sucesso na base de dados, dados: ' + 'id: ' + str(time.get_id()) + ', nome: ' + \
               time.get_nome()

    def exclude_jogador(self, id_jogador):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        values = str(id_jogador)
        sql = f"DELETE from Time j where id_time = '{values}'"
        cursor.execute(sql)
        db_connection.commit()
        return 'Time excluido com sucesso com id: ' + str(id_jogador)
