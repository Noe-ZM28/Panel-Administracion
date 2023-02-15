import os
class tools:
    def __init__ (self, ruta_proyecto = None):
        # Ruta del directorio a listar
        self.ruta_proyecto = self.get_project_path()
    
    @staticmethod
    def get_project_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def listar_directorios_archivos(self):
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




# Llamada a la función para listar los directorios y archivos del proyecto
ayuda = tools()
#ayuda.listar_directorios_archivos()