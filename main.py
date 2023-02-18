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


# import tkinter as tk
# from tkinter import ttk
# from tkcalendar import Calendar

# def obtener_fecha():
#     fecha_seleccionada = cal.selection_get().strftime('%Y-%m-%d')
#     print(fecha_seleccionada)
#     root.destroy()

# root = tk.Tk()
# root.title("Calendario")
# root.geometry("300x250")

# # Centrar la ventana en la pantalla
# windowWidth = root.winfo_reqwidth()
# windowHeight = root.winfo_reqheight()
# positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
# positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
# root.geometry("+{}+{}".format(positionRight, positionDown))

# cal = Calendar(root, selectmode="day")
# cal.pack(pady=20)

# button = ttk.Button(root, text="Seleccinar Fecha", command=obtener_fecha)
# button.pack(pady=10)

# root.mainloop()



import tkinter as tk
from tktimepicker import AnalogPicker, AnalogThemes
# note: you can also make use of mouse wheel or keyboard to scroll or enter the spin timepicker
root = tk.Tk()

time_picker = AnalogPicker(root)
time_picker.pack(expand=True, fill="both")

theme = AnalogThemes(time_picker)
theme.setDracula()

root.mainloop()


