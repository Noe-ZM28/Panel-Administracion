import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)

from Views.view_panel_entradas import Panel_Entradas
from Views.view_login import Login

theme_aquativo = 'aquativo'
theme_arc = 'arc'
theme_black = 'black'
theme_blue = 'blue'
theme_breeze = 'breeze'
theme_clearlooks = 'clearlooks'
theme_elegance = 'elegance'
theme_equilux = 'equilux'
theme_itft1 = 'itft1'
theme_kroc = 'kroc'
theme_plastik = 'plastik'
theme_radiance = 'radiance'
theme_scidblue = 'scidblue'
theme_smog = 'smog'
theme_ubuntu = 'ubuntu'
theme_winxpblue = 'winxpblue'

#Ejemplo para correr el panel
app = Panel_Entradas('black')

