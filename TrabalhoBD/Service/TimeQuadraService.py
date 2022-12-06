from DBConf.DBConfig import DBConfig


class TimeQuadraService:
    dbConfig = DBConfig()

    def reservar_horario(self, id_time, id_quadra, horario):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = f"SELECT * FROM Time WHERE id_time = '{id_time}'"
        cursor.execute(sql)
        if cursor is None:
            return f'Não existe time com o id {str(id_time)}'
        else:
            sql_time = f"SELECT * FROM Quadra_Esportiva WHERE id_quadra = '{id_quadra}'"
            cursor.execute(sql_time)
            if cursor is None:
                return f'Não existe Quadra Esportiva com o id = {id_quadra}'
            else:
                sql_insert = f"INSERT INTO Time_Quadra (id_time, id_quadra, Horario_reservado) values " \
                             f"('{id_time}', '{id_quadra}', '{horario}')"
                cursor.execute(sql_insert)
                db_connection.commit()
                db_connection.close()
                return f'Horario reservado de {horario} ao time de id: {id_time} na ' \
                       f'quadra de id: {id_quadra}'
