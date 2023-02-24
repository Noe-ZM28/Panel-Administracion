import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image


from Config.config_tools import tools



class Login:
    def __init__(self):
        '''
        Constructor de la clase. Crea la ventana principal, de 
        '''

        # Crea la ventana principal
        self.window_login = tk.Tk()

        #temas xd
        style = ThemedStyle(self.window_login)
        #style.theme_use('black')


        # Establece el tamaño de la ventana y su título
        self.window_login.geometry()
        self.window_login.title(f'Login')


        # Crea las variables
        self.user = None
        self.password = None
        self.type_user = None

        tools_instance = tools()
        logo_pase = tools_instance.read_path_config_file('images', 'logo_pase')
        self.logo_pase = ImageTk.PhotoImage(Image.open(logo_pase))


        self.interface()

        # Inicia el loop principal de la ventana
        self.window_login.mainloop()

    def interface(self):
        # inserta el logo de la empresa
        logo = ttk.Label(self.window_login, image=self.logo_pase)
        logo.grid(row=0, column=0)

        # Crear una seccion para el formulario
        seccion_formulario = ttk.LabelFrame(self.window_login, text='', padding=10)
        seccion_formulario.grid(row=1, column=0, sticky='n')


        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de folio
        # etiqueta_folio = ttk.Label(seccion_consulta, text='Folio: ')
        # etiqueta_folio.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto el user
        self.campo_user = tk.Entry(seccion_formulario, textvariable=self.user)
        self.campo_user.grid(row=0, column=0, padx=5, pady=5)

        # Crear los campos de texto la contraseña
        self.campo_password = tk.Entry(seccion_formulario, textvariable=self.password)
        self.campo_password.grid(row=1, column=0, padx=5, pady=5)
        #######################################################################---














        

    def comprobar_user(self, user, password):
        pass
