import json

class DatabaseConfig:
    """
    Clase que representa la configuración de la base de datos.
    """

    def guardar_configuracion(self, name_config, host, user, password, database):

        """
        Guarda la configuración de la base de datos en un archivo JSON.

        :raises FileNotFoundError: Si no se encuentra el archivo de configuración.
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
            with open(r"Config/config_files/settings_database.json", "r") as f:
                settings = json.load(f)
        except FileNotFoundError:
            settings = {"settings": []}

        # Agrega la nueva configuración al diccionario de configuraciones
        settings['settings'].append(configuracion)

        # Guarda el diccionario de configuraciones en el archivo JSON
        with open(r"Config/config_files/settings_database.json", "w") as f:
            json.dump(settings, f, indent=4)


    def obtener_configuracion(self, name_config):
        with open(r"Config/config_files/settings_database.json", "r") as f:
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



# configuracion = DatabaseConfig()
# configuracion.guardar_configuracion("aaaaaaa", "localhost", "usuario1", "clave1", "basedatos1")
