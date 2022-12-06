from DBConf.DBConfig import DBConfig
from Model.Clube import Clube


class ClubeService:

    dbConfig = DBConfig()

    def create_clube(self, nome_clube, endereco_clube):
        clube = Clube(nome_clube, endereco_clube)
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = "INSERT INTO Clube (Nome, Id_clube, Endereco) VALUES (%s, %s, %s)"
        values = (clube.get_nome(), clube.get_id(), clube.get_endereco())
        cursor.execute(sql, values)
        db_connection.commit()
        return 'Clube criado com sucesso na base de dados, dados: ' + 'id: ' + str(clube.get_id()) + ', nome: ' + \
               clube.get_nome()

    def exclude_clube(self, id_clube):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        values = str(id_clube)
        sql = f"DELETE from Clube c where Id_clube = '{values}'"
        cursor.execute(sql)
        db_connection.commit()
        return 'Clube excluido com sucesso com id: ' + str(id_clube)
