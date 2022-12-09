from DBConf.DBConfig import DBConfig


class ContratanteQuadraService:
    dbConfig = DBConfig()

    def reservar_horario(self, id_contratante, id_quadra, horario):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = f"SELECT * FROM Contratante WHERE id_contratante = '{id_contratante}'"
        cursor.execute(sql)
        if cursor is None:
            return f'Não existe contratante com o id {str(id_contratante)}'
        else:
            sql_time = f"SELECT * FROM Quadra_Esportiva WHERE id_quadra = '{id_quadra}'"
            cursor.execute(sql_time)
            if cursor is None:
                return f'Não existe Quadra Esportiva com o id = {id_quadra}'
            else:
                sql_insert = f"INSERT INTO Contratante_Quadra (id_contratante, id_quadra, Horario_reservado) values " \
                             f"('{id_contratante}', '{id_quadra}', '{horario}')"
                cursor.execute(sql_insert)
                db_connection.commit()
                db_connection.close()
                return f'Horario reservado de {horario} ao contratante de id: {id_contratante} na ' \
                       f'quadra de id: {id_quadra}'
