# -*- coding: utf-8 -*-
import pymysql
import json

#from Config.config_database import DatabaseConfig

import sys
import os

# Obtener la ruta del directorio que contiene el archivo actual
dir_path = os.path.dirname(os.path.abspath(__file__))


def get_project_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Agregar el directorio 'Panel-Administracion' a la ruta de búsqueda de módulos de Python
sys.path.append(os.path.join(dir_path, '..', r'C:\Users\brink\Downloads\#Z\WORKSPACE\Panel-Administracion'))

# Ahora deberías poder importar la clase DatabaseConfig
from Config.config_database import DatabaseConfig


class database_connection:
    """
    Esta clase permite la conexión a una base de datos MySQL específica.
    Incluye métodos para conectarse a la base de datos, cerrar la conexión y ejecutar consultas en la base de datos.
    """

    def __init__ (self, config_db = None):
        self.config_db = DatabaseConfig()

        self.connection = None
        self.connect()

    def connect(self, name_config="Configuracion 1"):
        """
        Realiza la conexión a la base de datos de MySQL con los parámetros especificados en el archivo de configuración.
        Asigna el objeto de conexión a una variable de instancia `connection`.
        """
        configuracion = self.config_db.obtener_configuracion(name_config = "Configuracion 1")


        try:
            # Realiza la conexión a la base de datos
            self.connection = pymysql.connect(
                host=configuracion["host"],
                user=configuracion["user"],
                password=configuracion["password"],
                database=configuracion["database"]
            )
            
        except pymysql.err.OperationalError as e:
                print(f"Error: {e}")

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
