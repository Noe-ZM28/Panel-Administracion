import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)

from Views.view_panel_administracion import View_Panel_Administracion
from Views.view_select_conection import Conect
from Views.view_login import Login
from Views.view_calendar import Calendar
user_name='Test'

#View_Panel_Administracion(estacionamiento = 'Configuracion prueba-1',user_name = user_name)
#Conect(user_name=user_name)
Login()
