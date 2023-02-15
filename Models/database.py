import pymysql
import json


class database_connection:
    """
    Esta clase permite la conexión a una base de datos MySQL específica.
    Incluye métodos para conectarse a la base de datos, cerrar la conexión y ejecutar consultas en la base de datos.
    """

    def __init__ (self):
        self.connection = None
        self.connect()


    def connect(self, name_config="Configuracion 1"):
        """
        Realiza la conexión a la base de datos de MySQL con los parámetros especificados en el archivo de configuración.
        Asigna el objeto de conexión a una variable de instancia `connection`.
        """
        with open("Config\config_files\configuracion_database.json", "r") as f:
            data = json.load(f)

        # Obtiene la configuración seleccionada
        configuracion = None
        for config in data["settings"]:
            if config["name_config"] == name_config:
                configuracion = config
                break

        if configuracion is None:
            raise ValueError("No se encontró la configuración especificada.")

        # Realiza la conexión a la base de datos
        self.connection = pymysql.connect(
            host=configuracion["host"],
            user=configuracion["user"],
            password=configuracion["password"],
            database=configuracion["database"]
        )


    def close_connection(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.connection.close()


    def execute_query(self, query: str, values = None):
        """
        Ejecuta una consulta en la base de datos.

        :param query: Consulta SQL a ejecutar.
        :param values: Valores a ser utilizados en la consulta.
        """
        cursor = self.connection.cursor()
        # Si se pasaron valores, se ejecuta la consulta con esos valores
        if values is not None:
            cursor.execute(query, values)

        # Si no se pasaron valores, se ejecuta la consulta sin ellos
        else:
            cursor.execute(query)

        result = cursor.fetchall()    
        self.connection.commit()
        cursor.close()
        #self.close_connection()

        return result
