from Controller.controller_select_conection import Controller_Select_Conection
from Config.config_tools import tools

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar

from ttkthemes import ThemedStyle

from PIL import ImageTk, Image


class Conect:
    def __init__(self, theme=None, user_name = None):
        '''
        La clase Conect se encarga de crear una ventana para seleccionar una conexión.
        Permite al usuario seleccionar una conexión de una lista desplegable y conectarla mediante un botón.
        La ventana se ajusta al centro de la pantalla y contiene un logo de la empresa.
        Al cerrar la ventana se muestra un mensaje de despedida al usuario.
        '''
        self.user_name = user_name
        #Crea la ventana principal
        self.panel_connect = tk.Toplevel()

        #Si hay un tema seleccionado, se establece
        self.theme = theme
        if self.theme != None:
            style = ThemedStyle(self.panel_connect)
            style.theme_use(self.theme)

        #Establece el tamaño de la ventana y su título


        #Calcula la posición de la ventana en la pantalla
        pos_x = int(self.panel_connect.winfo_screenwidth()/2)
        pos_y = int(self.panel_connect.winfo_screenheight()/2)

        #Establece la geometría de la ventana con su posición y tamaño
        self.panel_connect.geometry(f"+{pos_x}+{pos_y}")
        self.panel_connect.resizable(False, False)
        self.panel_connect.title(f'Selecciona la conexión')

        #Configura la columna principal del panel para que use todo el espacio disponible
        self.panel_connect.columnconfigure(0, weight=1)

        #Crea las instancias de las clases tools() y Controller_Select_Conection()
        self.tools_instance = tools()
        self.select_controller = Controller_Select_Conection()

        #Crea las variables para los iconos e imagenes
        logo = self.tools_instance.read_path_config_file('images', 'logo_pase')
        logo_pase = Image.open(logo)
        logo_pase = logo_pase.resize((106, 55), Image.ANTIALIAS) # Cambiar tamaño de la imagen
        self.logo_pase = ImageTk.PhotoImage(logo_pase)

        self.variable_estacionamiento = StringVar()

        #Llama a la función interface() que configura la interfaz gráfica
        self.interface()

        #Inicia el loop principal de la ventana
        self.panel_connect.mainloop()

    def interface(self):
        """
        Crea toda la interface para cambiar de conexion
        """
        # Se crea un Label Frame principal para la sección superior
        seccion_superior = ttk.LabelFrame(self.panel_connect, text='')
        seccion_superior.columnconfigure(1, weight=1)
        seccion_superior.propagate(True)
        seccion_superior.grid(row=0, column=0, sticky="nsew")

        # Se crea otro Label Frame para la sección del logo dentro del Label Frame principal
        seccion_logo = ttk.LabelFrame(seccion_superior, text='')
        seccion_logo.grid(row=0, column=0, sticky=tk.NSEW)

        # Se crea una etiqueta con la imagen del logo dentro del Label Frame de la sección del logo
        etiqueta_logo = tk.Label(seccion_logo, image=self.logo_pase)
        etiqueta_logo.grid(row=0, column=0, sticky=tk.NSEW)

        # Se crea un Label Frame para la sección de la conexión
        seccion_conecion = ttk.LabelFrame(self.panel_connect, text='Selecciona la conexión')
        seccion_conecion.columnconfigure(1, weight=1)
        seccion_conecion.propagate(True)
        seccion_conecion.grid(row=1, column=0)

        # Se definen las opciones de conexión y se crea una ComboBox para seleccionar una opción
        etiqueta_bienvenida = ttk.Label(seccion_conecion, text=f'Bienvenido/a: {self.user_name}')
        etiqueta_bienvenida.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        opciones_conexiones = [
                                'Conexion Prueba',
                                # 'Ciudad Mendoza',
                                # 'Durango',
                                # 'Monterrey',
                                'Pino Suarez',
                                # 'Tenayuca'
                                ]
        self.lista_desplegable_opciones = ttk.Combobox(seccion_conecion, values=opciones_conexiones, textvariable=self.variable_estacionamiento, state='readonly', width = 30, height = 5)
        self.lista_desplegable_opciones.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.lista_desplegable_opciones.configure(foreground="black")

        # Se crea un Label Frame para la sección de los botones
        seccion_botones = ttk.LabelFrame(self.panel_connect, text='')
        seccion_botones.grid(row=2, column=0, sticky="nsew")

        # Se crea un botón para salir de la aplicación
        self.boton_salir = ttk.Button(seccion_botones, text='SALIR', command = self.salir)
        self.boton_salir.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

        # Se crea un botón para conectarse a la opción seleccionada
        self.boton_seleccionar = ttk.Button(seccion_botones, text='CONECTAR', 
            command = lambda: {
                # Se deshabilitan los botones mientras se realiza la conexión
                self.desactivar_botones(),

                # Se llama al método conectar del objeto select_controller con la opción seleccionada
                self.select_controller.conectar(estacionamiento= str(self.variable_estacionamiento.get()), user_name = self.user_name),
                # Se habilitan de nuevo los botones
                self.activar_botones(),
            })

        self.boton_seleccionar.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)



    def salir(self):
        """
        Muestra un cuadro de diálogo para informar al usuario que se está cerrando la aplicación y destruye el panel principal.
        """
        # Muestra un cuadro de diálogo con el mensaje "Hasta pronto"
        messagebox.showinfo('Salida', 'Hasta pronto.')
        # Detiene el loop principal
        self.panel_connect.quit()
        # Destruye el panel principal
        self.panel_connect.destroy()

        # Sale del programa
        raise SystemExit


    def desactivar_botones(self):
        """
        Desactiva los botones de la interface
        """
        self.boton_seleccionar.config(state="disable")
        self.boton_salir.config(state="disable")


    def activar_botones(self):
        """
        Activa los botones de la interface
        """
        self.boton_seleccionar.config(state="normal")
        self.boton_salir.config(state="normal")
