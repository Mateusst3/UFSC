from DBConf.DBConfig import DBConfig


class JogadorTimeService:
    dbConfig = DBConfig()

    def adicionar_ao_time(self, id_jogador, id_time):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = f"SELECT (Nome) FROM Jogador WHERE id_jogador = '{id_jogador}'"
        cursor.execute(sql)
        if cursor is None:
            return f'Não existe jogador com o id {str(id_jogador)}'
        else:
            sql_time = f"SELECT (Nome) FROM Time WHERE id_time = '{id_time}'"
            cursor.execute(sql_time)
            if cursor is None:
                return f'Não existe time com o id = {id_time}'
            else:
                sql_insert = f"INSERT INTO Jogador_Time (id_jogador, id_time) values " \
                            f"('{id_jogador}', '{id_time}')"
                cursor.execute(sql_insert)
                db_connection.commit()
                db_connection.close()
                return f'Jogador de id: {id_jogador} adicionado ao time de id: {id_time}'

    def excluir_do_time(self, id_jogador, id_time):
        db_connection = self.dbConfig.open_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = f"SELECT (Nome) FROM Jogador WHERE id_jogador = '{id_jogador}'"
        cursor.execute(sql)
        if cursor is None:
            return f'Não existe jogador com o id {str(id_jogador)}'
        else:
            sql_time = f"SELECT (Nome) FROM Time WHERE id_time = '{id_time}'"
            cursor.execute(sql_time)
            if cursor is None:
                return f'Não existe time com o id = {id_time}'
            else:
                sql_insert = f"DELETE FROM Jogador_Time WHERE id_jogador={id_jogador} AND id_time={id_time}"
                cursor.execute(sql_insert)
                db_connection.commit()
                db_connection.close()
                return f'Jogador de id: {id_jogador} adicionado ao time de id: {id_time}'

