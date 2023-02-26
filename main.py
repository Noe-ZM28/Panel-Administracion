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
# from tkinter import ttk

# root = tk.Tk()

# main_frame = ttk.LabelFrame(root, text="Mi LabelFrame Principal")
# main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# frame_1 = ttk.LabelFrame(main_frame, text="Frame 1")
# frame_1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

# tk.Label(frame_1, text="Etiqueta 1 dentro de Frame 1").grid(row=0, column=0)

# frame_2 = ttk.LabelFrame(main_frame, text="Frame 2")
# frame_2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

# tk.Label(frame_2, text="Etiqueta 1 dentro de Frame 2").grid(row=0, column=0)
# tk.Label(frame_2, text="Etiqueta 2 dentro de Frame 2").grid(row=1, column=0)

# frame_3 = ttk.LabelFrame(main_frame, text="Frame 3")
# frame_3.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

# tk.Label(frame_3, text="Etiqueta 1 dentro de Frame 3").grid(row=0, column=0)
# tk.Label(frame_3, text="Etiqueta 2 dentro de Frame 3").grid(row=1, column=0)
# tk.Label(frame_3, text="Etiqueta 3 dentro de Frame 3").grid(row=2, column=0)

# # Nuevo LabelFrame en la misma fila que el principal
# extra_frame = ttk.LabelFrame(root, text="Mi LabelFrame Extra")
# extra_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# tk.Label(extra_frame, text="Etiqueta dentro de LabelFrame Extra").grid(row=0, column=0)

# root.mainloop()
