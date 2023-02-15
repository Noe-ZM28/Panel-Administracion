from Models.database import database_connection


class Querys:
    """
    Esta clase contiene métodos para ejecutar consultas a una base de datos mediante una conexión establecida con la clase
    `database_connection`.
    """
    def __init__ (self, data_base = None):
        self.data_base = database_connection()

    def obtener_campos_tabla(self, tabla):
        """
        Obtiene los nombres de los campos en una tabla especificada.

        :param tabla: Nombre de la tabla.
        :return: Lista de los nombres de los campos en la tabla.
        """
        query = f"DESCRIBE {tabla}"
        resultado = self.data_base.execute_query(query)
        campos = [r[0] for r in resultado]
        return list(campos)

    def obtener_registros(self, table):
        """
        Obtiene todos los registros de una tabla especificada.

        :param table: Nombre de la tabla.
        :return: Todos los registros de la tabla.
        """
        query = f"select * from {table};"
        registros = self.data_base.execute_query(query)
        return registros
