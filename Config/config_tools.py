import os
import json

class tools:
    """
    Clase que proporciona herramientas útiles para el proyecto.
    """

    def __init__(self, ruta_proyecto=None):
        """
        Constructor de la clase.

        :param ruta_proyecto: La ruta del directorio raíz del proyecto.
        """
        self.ruta_proyecto = self.get_project_path()

    @staticmethod
    def get_project_path():
        """
        Método que obtiene la ruta del directorio raíz del proyecto.

        :return: La ruta del directorio raíz del proyecto.
        """
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def listar_directorios_archivos(self):
        """
        Método que imprime una lista de todos los archivos y directorios dentro del directorio raíz del proyecto,
        excluyendo la carpeta "env", archivos ocultos y la carpeta ".git".
        """
        for root, dirnames, filenames in os.walk(self.ruta_proyecto):
            # Ignorar la carpeta "env"
            if 'env' in dirnames:
                dirnames.remove('env')
            if '.git' in dirnames:
                dirnames.remove('.git')
            if '__pycache__' in dirnames:
                dirnames.remove('__pycache__')
            level = root.replace(self.ruta_proyecto, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 4 * (level + 1)
            # Ignorar archivos ocultos
            for f in filenames:
                if not f.startswith('.'):
                    print(f"{subindent}{f}")

    def read_path_config_file(self, type_file, file_path):
        """
        Método que lee la ruta de un archivo de configuración desde un archivo JSON.

        :param file: El nombre del archivo de configuración.
        :return: La ruta del archivo de configuración.
        """
        json_path = r'Config\config_files\settings_path_files.json'
        try:
            with open(json_path) as f:
                data = json.load(f)
                return data['path_files'][0][type_file][0][file_path]
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no se pudo abrir.")
            return None
