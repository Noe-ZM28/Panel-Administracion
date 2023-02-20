import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)


from Views.view_panel_entradas import Panel_Entradas
from Views.views_tools import Fecha_Hora


#Ejemplo para correr el panel
app = Panel_Entradas()
