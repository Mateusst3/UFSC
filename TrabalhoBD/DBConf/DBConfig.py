from mysql.connector import (connection)
from mysql.connector import errorcode


class DBConfig:

    def open_connection(self):
        return connection.MySQLConnection(host='localhost', user='root', password='',
                                                        database='TrabalhoBd')
