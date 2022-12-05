from Model.Jogador import Jogador
from DBConf.DBConfig import DBConfig


class JogadorService:

    dbConfig = DBConfig()

    def create_jogador(self, nome_jogador):
        jogador = Jogador(nome_jogador)
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = "INSERT INTO Jogador (Nome, id_jogador) VALUES (%s, %s)"
        values = (jogador.get_nome(), jogador.get_id())
        cursor.execute(sql, values)
        db_connection.commit()
        return 'Jogador criado com sucesso na base de dados, dados: ' + 'id: ' + str(jogador.get_id()) + ', nome: ' + \
               jogador.get_nome()

    def exclude_jogador(self, id_jogador):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        values = str(id_jogador)
        sql = f"DELETE from Jogador j where id_jogador = '{values}'"
        cursor.execute(sql)
        db_connection.commit()
        return 'Jogador excluido com sucesso com id: ' + str(id_jogador)
