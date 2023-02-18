import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)


from Views.view_panel_entradas import Panel_Entradas
from Views.views_tools import Fecha_Hora
from Views.views_tools import CalendarButton


#Ejemplo para correr el panel
#app = Panel_Entradas()


# app = Fecha_Hora()
# app.selected_datetime


import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear un botón de calendario
calendar_button = CalendarButton(root)
calendar_button.pack()

# Mostrar la ventana
root.mainloop()