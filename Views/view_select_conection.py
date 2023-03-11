from Controller.controller_select_conection import SelectController

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import PhotoImage
from tkinter import Spinbox

from PIL import ImageTk, Image


from Config.config_tools import tools


from ttkthemes import ThemedStyle


class Conect:
    '''Clase principal que maneja la interfaz gráfica del usuario para seleccionar la conexion.'''
    def __init__(self, theme=None):
        '''
        Constructor de la clase. Crea la ventana principal
        '''
        # Establece la tabla que se visualizará por defecto
        self.ver_tabla = 'Entradas'

        # Crea la ventana principal
        self.panel_connect = tk.Tk()

        self.theme = theme
        if self.theme != None:
            #temas xd
            style = ThemedStyle(self.panel_connect)
            style.theme_use(self.theme)

        # ancho_max = self.panel_connect.winfo_screenwidth()
        # alto_max = self.panel_connect.winfo_screenheight()
        # self.panel_connect.wm_maxsize(ancho_max, alto_max)

        # Establece el tamaño de la ventana y su título
        self.panel_connect.geometry()
        #self.panel_connect.resizable(False, False)

        self.panel_connect.title(f'Selecciona la conexión')

        # Configura la columna principal del panel para que use todo el espacio disponible
        self.panel_connect.columnconfigure(0, weight=1)

        self.tools_instance = tools()
        self.select_controller = SelectController()
        # Crea las variables para los iconos e imagenes
        logo = self.tools_instance.read_path_config_file('images', 'logo_pase')
        logo_pase = Image.open(logo)
        logo_pase = logo_pase.resize((106, 55), Image.ANTIALIAS)  # Cambiar tamaño de la imagen
        self.logo_pase = ImageTk.PhotoImage(logo_pase)

        self.variable_estacionamiento = StringVar()


        self.interface()
        # Inicia el loop principal de la ventana
        self.panel_connect.mainloop()

    def interface(self):
        #Label frame principal
        seccion_superior = ttk.LabelFrame(self.panel_connect, text='')
        seccion_superior.columnconfigure(1, weight=1)
        seccion_superior.propagate(True)
        seccion_superior.grid(row=0, column=0, sticky=tk.NSEW)

        seccion_logo = ttk.LabelFrame(seccion_superior, text='')
        seccion_logo.grid(row=0, column=0, sticky=tk.NSEW)

        etiqueta_logo = tk.Label(seccion_logo, image=self.logo_pase)
        etiqueta_logo.grid(row=0, column=0, sticky=tk.NSEW)

        seccion_conecion = ttk.LabelFrame(self.panel_connect, text='Selecciona la conexión')
        seccion_conecion.columnconfigure(1, weight=1)

        seccion_conecion.propagate(True)
        seccion_conecion.grid(row=1, column=0, sticky=tk.NSEW)

        opciones_conexiones = [
                                'Oficina Chiapas', 
                                'Ciudad Mendoza', 
                                'Durango', 
                                'Monterrey', 
                                'Pino Suarez', 
                                'Tenayuca']

        self.lista_desplegable_opciones = ttk.Combobox(seccion_conecion, values=opciones_conexiones, textvariable=self.variable_estacionamiento, state='readonly', width = 25, height = 5)
        self.lista_desplegable_opciones.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.lista_desplegable_opciones.configure(foreground="black")

        seccion_botones = ttk.LabelFrame(self.panel_connect, text='')
        seccion_botones.grid(row=2, column=0, sticky=tk.NSEW)

    
        boton_seleccionar = ttk.Button(seccion_botones, text='CONECTAR', 
            command = lambda: {
                self.select_controller.conectar(str(self.variable_estacionamiento.get()))
            })
        boton_seleccionar.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)

        boton_salir = ttk.Button(seccion_botones, text='SALIR', command = self.salir)
        boton_salir.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

    def desconectar(self):
        pass

    def salir(self):
        """
        Muestra un cuadro de diálogo para informar al usuario que se está cerrando la aplicación y destruye el panel principal.
        """
        # Muestra un cuadro de diálogo con el mensaje "Hasta pronto"
        messagebox.showinfo('Salida', 'Hasta pronto.')
        
        #detener el loop principal
        self.panel_connect.quit()
        # Destruye el panel principal
        self.panel_connect.destroy()


