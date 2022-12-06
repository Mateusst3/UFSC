from DBConf.DBConfig import DBConfig


class ContratanteClubeService:
    dbConfig = DBConfig()

    def reservar_horario(self, id_contratante, id_clube, horario):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = f"SELECT (Nome) FROM Contratante WHERE id_contratante = '{id_contratante}'"
        cursor.execute(sql)
        if cursor is None:
            return f'Não existe contratante com o id {str(id_contratante)}'
        else:
            sql_time = f"SELECT (Nome) FROM Clube WHERE id_time = '{id_clube}'"
            cursor.execute(sql_time)
            if cursor is None:
                return f'Não existe Clube com o id = {id_clube}'
            else:
                sql_insert = f"INSERT INTO Contratante_Clube (id_contratante, id_clube, Horario_resevado) values " \
                             f"('{id_contratante}', '{id_clube}', '{horario}')"
                cursor.execute(sql_insert)
                db_connection.commit()
                db_connection.close()
                return f'Horario reservado de {horario} ao contratante de id: {id_contratante} no ' \
                       f'clube de id: {id_clube}'
