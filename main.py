import os
import sys

from Views.view_panel_entradas import Panel_Entradas
from Config.config_database import DatabaseConfig
from Models.queries import Queries

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)


#Ejemplo para correr el panel
app = Panel_Entradas()



# consulta = Queries()
# consulta.crear_consulta_sql_entradas(fecha_inicio_entrada = "2022-01-01", fecha_fin_entrada = "2023-01-01", fecha_inicio_salida = "2022-01-01", fecha_fin_salida = "2023-01-01")




# if __name__ == "__main__":
#     app = Aplicacion("cortes")