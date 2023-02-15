import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()

# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)

from Views.view_panel import Aplicacion
from Config.config_database import DatabaseConfig


#Ejemplo para correr el panel
app = Aplicacion("cortes")




#Ejemplo para añadir nuevas configuraciones
# configuracion = DatabaseConfig()
# configuracion.guardar_configuracion("aaaaaaa", "localhost", "usuario1", "clave1", "basedatos1")






# if __name__ == "__main__":
#     app = Aplicacion("cortes")