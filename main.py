import os
import sys

# Obtener el directorio raíz del proyecto
proyecto_dir = os.getcwd()
# Agregar el directorio raíz del proyecto al path de Python
sys.path.append(proyecto_dir)

from Views.view_panel_entradas import Panel_Entradas
from Views.view_login import Login

#app = Login()

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
app = Panel_Entradas()

# import tkinter as tk

# root = tk.Tk()

# # Crear el primer LabelFrame y agregar algunos widgets
# lf1 = tk.LabelFrame(root, text="LabelFrame 1", padx=10, pady=10)
# lf1.grid(row=0, column=0, sticky="NW")
# tk.Label(lf1, text="Widget 1").grid(row=0, column=0)
# tk.Label(lf1, text="Widget 2").grid(row=1, column=0)

# # Crear el segundo LabelFrame y agregar algunos widgets
# lf2 = tk.LabelFrame(root, text="LabelFrame 2", padx=10, pady=10)
# lf2.grid(row=0, column=1, sticky="NW")
# tk.Label(lf2, text="Widget 3").grid(row=0, column=0)
# tk.Label(lf2, text="Widget 4").grid(row=1, column=0)
# tk.Label(lf2, text="Widget 5").grid(row=2, column=0)

# root.mainloop()
