import os
import sys

from Views.view_panel_entradas import Panel_Entradas

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)


#Ejemplo para correr el panel
app = Panel_Entradas()
