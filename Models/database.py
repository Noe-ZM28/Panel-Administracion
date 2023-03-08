import pymysql
from pymysql import err
import json
from tkinter import messagebox


from Config.config_database import DatabaseConfig


class database_connection:
    """
    Esta clase permite la conexión a una base de datos MySQL específica.
    Incluye métodos para conectarse a la base de datos, cerrar la conexión y ejecutar consultas en la base de datos.
    """

    def __init__ (self, config_db = None):
        """
        Inicializa una instancia de la clase `database_connection`.

        :param config_db: Una instancia de la clase `DatabaseConfig`. Si no se proporciona, se crea una nueva instancia de la clase `DatabaseConfig`.
        """
        # Si no se proporciona una instancia de la clase `DatabaseConfig`, se crea una nueva instancia
        if config_db is None:
            self.config_db = DatabaseConfig()
        else:
            self.config_db = config_db

        # Inicializa el objeto de conexión a la base de datos
        self.connection = None
        self.cursor = None

        # Establece la conexión a la base de datos
        self.connect()

    def connect(self, name_config="Configuracion 1"):
        """
        Realiza la conexión a la base de datos de MySQL con los parámetros especificados en el archivo de configuración.
        Asigna el objeto de conexión a una variable de instancia `connection`.

        :param name_config: El nombre de la configuración a utilizar. Por defecto es "Configuracion 1".
        """
        # Obtiene la configuración de la base de datos desde el archivo de configuración
        configuracion = self.config_db.obtener_configuracion(name_config = name_config)

        try:
            # Realiza la conexión a la base de datos
            self.connection = pymysql.connect(
                host=configuracion["host"],
                user=configuracion["user"],
                password=configuracion["password"],
                database=configuracion["database"]
            )

            # Crea un objeto cursor para ejecutar la consulta

            # Si ocurre un error al conectarse a la base de datos, se muestra un mensaje de error en la consola
        except pymysql.err.OperationalError as e:
            messagebox.showwarning("Error",f"Error al conectarse a la base de datos, por favor asegusere de que introdujo un Host valido o que el Host al que se intenta conectar se encuentra activo.")
            raise SystemExit


    def close_connection(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.connection.close()

    def execute_query(self, query: str, values=None):
        """
        Ejecuta una consulta en la base de datos.

        :param query: La consulta SQL a ejecutar.
        :type query: str
        :param values: Valores a ser utilizados en la consulta. Por defecto es `None`.
        :type values: Any
        :return: Una lista con los resultados de la consulta.
        :return type: list
        """
        try:
            # Crea un objeto cursor para ejecutar la consulta
            self.cursor = self.connection.cursor()
            # Si se pasaron valores, se ejecuta la consulta con esos valores
            if values is not None:
                self.cursor.execute(query, values)
            # Si no se pasaron valores, se ejecuta la consulta sin ellos
            else:
                self.cursor.execute(query)

            # Obtiene los resultados de la consulta
            result = self.cursor.fetchall()

            # Confirma los cambios en la base de datos
            self.connection.commit()

            # Cierra el cursor
            self.cursor.close()

            # Retorna los resultados de la consulta
            return result

        except err.ProgrammingError:
            messagebox.showwarning("Error", f"Has ingresado un valor invalido para realizar la consulta, favor de revisar")

        except Exception as e:
            messagebox.showwarning("Error", f"Error al realizar la consulta, por favor contacte con un administrador y muestre el siguiente error:\n Error: {str(e)} ")
            return []
