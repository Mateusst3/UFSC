from DBConf.DBConfig import DBConfig
from Model.Contratante import Contratante


class ContratanteService:

    dbConfig = DBConfig()

    def create_contratante(self, nome, endereco, telefone):
        contratante = Contratante(nome, endereco, telefone)
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = "INSERT INTO Contratante (id_contratante, Nome, Endereco, Telefone) VALUES (%s, %s, %s, %s)"
        values = (contratante.get_id(), contratante.get_nome(), contratante.get_endereco(), contratante.get_telefone())
        cursor.execute(sql, values)
        db_connection.commit()
        return 'Contratante criado com sucesso na base de dados, dados: ' + 'id: ' + str(contratante.get_id()) + ', nome: ' + contratante.get_nome(), + ', endereço: ' + contratante.get_endereco() + ', telefone: ' + contratante.get_telefone()

    def exclude_contratante(self, id_contratante):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        values = str(id_contratante)
        sql = f"DELETE from Contratante where id_contratante = '{values}'"
        cursor.execute(sql)
        db_connection.commit()
        return 'Contratante excluido com sucesso com id: ' + str(id_contratante)
