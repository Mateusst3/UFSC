from Model.Jogador import Jogador
from DBConf.DBConfig import DBConfig


class JogadorService:

    dbConfig = DBConfig()

    def create_jogador(self, nome_jogador):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor()
        sql = "SELECT * FROM JOGADOR"
        cursor.execute(sql)
        db_connection.commit()
        db_connection.close()
        return 'teste'
