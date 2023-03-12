import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

from Config.config_tools import tools
from Controller.controller_login import ControllerLogin


class Login:
    def __init__(self):
        # Crea la ventana principal
        self.window_login = tk.Tk()

        #temas xd
        self.style = ThemedStyle(self.window_login)

        # Establece el tamaño de la ventana y su título
        self.window_login.title(f'Login')

        ancho_max = self.window_login.winfo_screenwidth()
        alto_max = self.window_login.winfo_screenheight()
        self.window_login.wm_maxsize(ancho_max, alto_max)

        pos_x = int(ancho_max/3)
        pos_y = int(alto_max/10)
        self.window_login.geometry(f"+{pos_x}+{pos_y}")
        self.window_login.resizable(False, False)

        # Crea las variables
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.theme = tk.StringVar()
        self.true_theme = tk.StringVar()

        tools_instance = tools()
        self.controller_login = ControllerLogin()

        # Crea las variables para los iconos e imagenes
        logo = tools_instance.read_path_config_file('images', 'logo_pase')
        logo_pase = Image.open(logo)
        logo_pase = logo_pase.resize((212, 110), Image.ANTIALIAS)  # Cambiar tamaño de la imagen
        self.logo_pase = ImageTk.PhotoImage(logo_pase)

        self.interface()

        # Inicia el loop principal de la ventana
        self.window_login.mainloop()

    def interface(self):
        self.seccion_principal = ttk.LabelFrame(self.window_login, text='')
        self.seccion_principal.grid(row=0, column=0, sticky=tk.NSEW)

        # inserta el logo de la empresa
        logo = ttk.Label(self.seccion_principal, image=self.logo_pase)
        logo.grid(row=0, column=0)

        # Crear una seccion para el formulario
        self.seccion_formulario = ttk.LabelFrame(self.seccion_principal, text='Ingresa los siguientes datos', padding=10)
        self.seccion_formulario.grid(row=1, column=0, sticky=tk.NSEW)

        #######################################################################---
        # Crear la leyenda para el campo de texto del nombre de ussuario
        etiqueta_user = ttk.Label(self.seccion_formulario, text='Nombre de usuario: ')
        etiqueta_user.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto el user
        campo_user = tk.Entry(self.seccion_formulario, textvariable=self.user)
        campo_user.grid(row=0, column=1, padx=5, pady=5)

        # Crear la leyenda para el campo de texto del nombre de ussuario
        etiqueta_user = ttk.Label(self.seccion_formulario, text='Contraseña: ')
        etiqueta_user.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto la contraseña
        campo_password = tk.Entry(self.seccion_formulario, textvariable=self.password)
        campo_password.grid(row=1, column=1, padx=5, pady=5)

        boton_entrar = ttk.Button(self.seccion_formulario, text='Entrar',
            command=lambda:self.controller_login.get_data(
                                                                theme = self.true_theme.get(),
                                                                usser = self.user.get(),
                                                                password = self.password.get()))

        boton_entrar.grid(row=0, column=2, padx=5, pady=5)

        # Crear una seccion para el formulario
        seccion_tema = ttk.LabelFrame(self.seccion_principal, text='Si lo deseas, selecciona un tema', padding=10)
        seccion_tema.grid(row=2, column=0, sticky=tk.NSEW)
        THEMES = [  
                    'default',
                    "adapta",
                    "aquativo",
                    "arc",
                    "black",
                    "blue",
                    "breeze",
                    "clearlooks",
                    "elegance",
                    "equilux",
                    "itft1",
                    "keramik",
                    "kroc",
                    "plastik",
                    "radiance",
                    "scidblue",
                    "scidgreen",
                    "scidgrey",
                    "scidmint",
                    "scidpink",
                    "scidpurple",
                    "scidsand",
                    "smog",
                    "ubuntu",
                    "winxpblue",
                    "yaru"
                ]

        lista_desplegable_tema = ttk.Combobox(seccion_tema,  values=THEMES, textvariable=self.theme, state='readonly', height=5)
        lista_desplegable_tema.grid(row=2, column=0, padx=5, pady=5)

        boton_tema = ttk.Button(seccion_tema, text='Ver tema', command=lambda:self.ver_tema(self.theme.get()))
        boton_tema.grid(row=2, column=1, padx=5, pady=5)

        boton_selecionar_tema = ttk.Button(seccion_tema, text='Seleccionar tema', command=self.seleccionar_tema)
        boton_selecionar_tema.grid(row=2, column=2, padx=5, pady=5)

    def ver_tema(self, theme = None):
        self.style.theme_use(theme)

    def seleccionar_tema(self):
        self.true_theme.set(self.theme.get())

