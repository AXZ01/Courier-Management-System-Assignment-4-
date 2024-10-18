import pyodbc
from .DBPropertyUtil import DBPropertyUtil


class DBConnUtil:
    @staticmethod
    def get_connection(config_file):
        try:
            connection_string = DBPropertyUtil.get_connection_string(
                config_file)
            conn = pyodbc.connect(connection_string)
            return conn
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            error_message = ex.args[1]
            print(f"Database connection failed with error: SQLState: {
                  sqlstate}, Error: {error_message}")
            return None
