import json
from Config.config_tools import tools

class DatabaseConfig:
    """
    Clase que representa la configuración de la base de datos.

    Atributos:
        tools_instance (tools): instancia de la clase tools
        database_config_file (str): ruta del archivo de configuración de la base de datos
    """

    def __init__ (self):
        """
        Inicializa una instancia de la clase DatabaseConfig.
        """
        self.tools_instance = tools()
        self.database_config_file = self.tools_instance.read_path_file("database_config_file")

    def guardar_configuracion(self, name_config, host, user, password, database):
        """
        Guarda la configuración de la base de datos en un archivo JSON.

        Args:
            name_config (str): nombre de la configuración
            host (str): dirección del servidor de la base de datos
            user (str): nombre de usuario para acceder a la base de datos
            password (str): contraseña para acceder a la base de datos
            database (str): nombre de la base de datos a la que conectarse

        Raises:
            FileNotFoundError: si no se encuentra el archivo de configuración.
        """
        # Crea un diccionario con los parámetros de la conexión
        configuracion = {
            "name_config": name_config,
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }

        try:
            # Intenta abrir el archivo de configuración existente
            with open(self.database_config_file, "r") as f:
                settings = json.load(f)
        except FileNotFoundError:
            settings = {"settings": []}

        # Agrega la nueva configuración al diccionario de configuraciones
        settings['settings'].append(configuracion)

        # Guarda el diccionario de configuraciones en el archivo JSON
        with open(self.database_config_file, "w") as f:
            json.dump(settings, f, indent=4)

    def obtener_configuracion(self, name_config):
        """
        Obtiene la configuración de la base de datos a partir de su nombre.

        Args:
            name_config (str): nombre de la configuración

        Returns:
            dict: un diccionario con los parámetros de la conexión a la base de datos.

        Raises:
            ValueError: si no se encuentra la configuración especificada.
        """
        with open(self.database_config_file, "r") as f:
            data = json.load(f)

        # Obtiene la configuración seleccionada
        configuracion = None
        for config in data["settings"]:
            if config["name_config"] == name_config:
                configuracion = config
                break

        if configuracion is None:
            raise ValueError("No se encontró la configuración especificada.")

        return configuracion
