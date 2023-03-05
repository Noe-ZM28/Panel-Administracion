import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import PhotoImage
from tkinter import Spinbox

from PIL import ImageTk, Image


from Config.config_tools import tools
from Models.queries import Queries


from ttkthemes import ThemedStyle


from Controller.controller_panel_entradas import EntradasController



class Panel_Entradas:
    '''Clase principal que maneja la interfaz gráfica del usuario.'''

    def __init__(self, theme=None):
        '''
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.
        '''
        # Establece la tabla que se visualizará por defecto
        self.ver_tabla = 'Entradas'

        # Crea la ventana principal
        self.panel = tk.Tk()

        self.theme = theme
        if self.theme != None:
            #temas xd
            style = ThemedStyle(self.panel)
            style.theme_use(self.theme)

        ancho_max = self.panel.winfo_screenwidth()
        alto_max = self.panel.winfo_screenheight() - 100
        self.panel.wm_maxsize(ancho_max, alto_max)

        # Establece el tamaño de la ventana y su título
        self.panel.geometry()
        #self.panel.resizable(False, False)

        self.panel.title(f'Panel de administración reporte general - Cortes')

        # Configura la columna principal del panel para que use todo el espacio disponible
        self.panel.columnconfigure(0, weight=1)

        # Crea las variables para la consulta simple

        self.variable_folio = StringVar()

        self.variable_tipo_tarifa_preferente = ''
        self.variable_tarifa_preferente = StringVar()

        self.variable_fecha_inicio_entrada = StringVar()
        self.variable_fecha_fin_entrada = StringVar()
        self.variable_fecha_inicio_salida = StringVar()
        self.variable_fecha_fin_salida = StringVar()

        self.variable_tiempo_dentro = StringVar()
        self.variable_tiempo_dentro_inicio = StringVar()
        self.variable_tiempo_dentro_fin = StringVar()

        self.variable_tipo_promocion = ''
        self.variable_promocion = StringVar()

        self.variable_corte_numero = StringVar()
        self.variable_corte_inicio = StringVar()
        self.variable_corte_fin = StringVar()

        self.variable_importe = StringVar()
        self.variable_importe_inicio = StringVar()
        self.variable_importe_final = StringVar()



        #instancia de la clase de herramientas
        tools_instance = tools()


        # Crea las variables para los iconos e imagenes
        logo = tools_instance.read_path_config_file('images', 'logo_pase')
        logo_pase = Image.open(logo)
        logo_pase = logo_pase.resize((106, 55), Image.ANTIALIAS)  # Cambiar tamaño de la imagen
        self.logo_pase = ImageTk.PhotoImage(logo_pase)


        icono_calendario = tools_instance.read_path_config_file('images', 'icono_calendario')
        self.icono_calendario = PhotoImage(file=icono_calendario).subsample(25)

        icono_salir = tools_instance.read_path_config_file('images', 'icono_salir')
        self.icono_salir = PhotoImage(file=icono_salir).subsample(50)

        icono_desconectar = tools_instance.read_path_config_file('images', 'icono_desconectar')
        self.icono_desconectar = PhotoImage(file=icono_desconectar).subsample(50)


        # Crea las variables para el manejo de calendario
        self.calendario_fecha_inicio_entrada = None
        self.fecha_hora_inicio_entrada = None
        self.calendario_fecha_fin_entrada = None
        self.fecha_hora_fin_entrada = None
        self.calendario_fecha_inicio_salida = None
        self.fecha_hora_inicio_salida = None
        self.calendario_fecha_fin_salida = None
        self.fecha_hora_fin_salida = None


        # Crea las variables para almacenar los registros y las consultas a la base de datos
        self.registros = None
        self.parametros = ''
        self.query = Queries()
        self.controlador_entrada = EntradasController(self.theme)
        self.message = None
        self.tabla = None


        # Crea la tabla y los campos de consulta
        self.view_tabla()
        self.view_campos_consulta()



        # Inicia el loop principal de la ventana
        self.panel.mainloop()

    def view_campos_consulta(self):
        '''Crea y empaqueta los campos de consulta en la ventana.'''
        #Label frame principal
        seccion_principal = ttk.LabelFrame(self.panel, text='')
        seccion_principal.columnconfigure(1, weight=1)
        #seccion_principal.grid_propagate(True)
        seccion_principal.propagate(True)
        seccion_principal.grid(row=0, column=0, sticky=tk.NSEW)


        seccion_logo = ttk.LabelFrame(seccion_principal, text='')
        seccion_logo.grid(row=0, column=0, sticky=tk.NW)

        etiqueta_logo = tk.Label(seccion_logo, image=self.logo_pase)
        etiqueta_logo.grid(row=0, column=0, sticky=tk.NW)

        #Label frame para seleccionar el tipo de consulta
        seccion_menu_consulta = ttk.LabelFrame(seccion_principal, text='Selecciona tipo de consulta', padding=10)
        seccion_menu_consulta.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        boton_campos_simple = ttk.Button(seccion_menu_consulta, text='Consulta simple', command=self.mostrar_campos_simple)
        boton_campos_simple.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=5)

        boton_ver_todo = ttk.Button(seccion_menu_consulta, text='Consulta avanzado', command=self.mostrar_campos_avanzado)
        boton_ver_todo.grid(row=0, column=1, sticky=tk.NSEW, padx=5, pady=5)

        # Configurar las columnas intermedias con un tamaño mínimo
        seccion_menu_consulta.columnconfigure(3, minsize=100)
        seccion_menu_consulta.columnconfigure(4, minsize=100)
        seccion_menu_consulta.columnconfigure(5, minsize=100)

        boton_generar_reporte = ttk.Button(seccion_menu_consulta, text='Generar reporte', compound='left',
        command = lambda:
                        {
                            self.controlador_entrada.realizar_reporte(registros = self.registros, parametros = self.parametros),
                            self.vaciar_campos()
                        })
        boton_generar_reporte.grid(row=0, column=6, pady=5)


        # Crea un LabelFrame para los botones de desconectar y salir
        seccion_botones_salir = ttk.LabelFrame(seccion_principal, text='Salir')
        seccion_botones_salir.grid(row=0, column=3, padx=5, pady=5, sticky='NW')

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_desconectar = ttk.Button(seccion_botones_salir, text='Desconectar', command=self.desconectar,  image=self.icono_desconectar)
        boton_desconectar.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_salir = ttk.Button(seccion_botones_salir, text='Salir', command=self.salir, image=self.icono_salir)
        boton_salir.grid(row=0, column=1, pady=5)



        #Labelframe para el tipo de consulta a realizar
        self.seccion_formulario_datos = ttk.LabelFrame(seccion_principal, text='Ingresa los datos de la consulta', padding=10)


        #Labelframe para consultas simple
        self.seccion_consulta_simple = ttk.LabelFrame(self.seccion_formulario_datos, text='Formulario simple')

        def view_consulta_simple(self):
            seccion_formulario_simple = ttk.LabelFrame(self.seccion_consulta_simple, text='Consulta simple')
            seccion_formulario_simple.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
            #######################################################################---
            # Crear la leyenda para el campo de texto de la consulta de folio
            etiqueta_folio = ttk.Label(seccion_formulario_simple,  text='N° de boleto: ')
            etiqueta_folio.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

            # Crear los campos de texto para la consulta de folio
            self.campo_texto_folio = tk.Entry(seccion_formulario_simple,  textvariable=self.variable_folio)
            self.campo_texto_folio.grid(row=0, column=1, padx=5, pady=5)
            #######################################################################---

            #######################################################################---
            # Crear la leyenda para el campo de texto de la consulta de corte
            etiqueta_corte = ttk.Label(seccion_formulario_simple,  text='N° de corte: ')
            etiqueta_corte.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)


            opciones = self.query.obtener_lista_de('CorteInc', 'D')
            # Crear la lista desplegable
            self.lista_desplegable_corte = ttk.Combobox(seccion_formulario_simple,  values=opciones, textvariable=self.variable_corte_numero, state='readonly', height=5)
            self.lista_desplegable_corte.grid(row=1, column=1, padx=5, pady=5)
            #######################################################################---

            #######################################################################---
            # Crear la leyenda para el campo de texto de la consulta de corte
            etiqueta_tipo_tarifa = ttk.Label(seccion_formulario_simple,  text='Tipo de tarifa: ')
            etiqueta_tipo_tarifa.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)


            opciones = self.query.obtener_lista_de('TarifaPreferente')
            # Crear la lista desplegable
            self.lista_desplegable_tipo_tarifa_preferente = ttk.Combobox(seccion_formulario_simple,  values=opciones, textvariable=self.variable_tarifa_preferente, state='readonly')
            self.lista_desplegable_tipo_tarifa_preferente.grid(row=2, column=1, padx=5, pady=5)
            #######################################################################---


            #######################################################################---
            # Crear la leyenda para el campo de texto de la consulta de corte
            etiqueta_tipo_promocion = ttk.Label(seccion_formulario_simple,  text='Tipo de promoción: ')
            etiqueta_tipo_promocion.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)


            #opciones = self.query.obtener_lista_de('TarifaPreferente')
            opciones = self.query.obtener_lista_de('TipoPromocion')
            # Crear la lista desplegable
            self.lista_desplegable_tipo_promocion = ttk.Combobox(seccion_formulario_simple,  values=opciones, textvariable=self.variable_promocion, state='readonly')
            self.lista_desplegable_tipo_promocion.grid(row=3, column=1, padx=5, pady=5)

            #######################################################################---



            # Crea un LabelFrame para los botones de desconectar y salir
            seccion_botones_consulta = ttk.LabelFrame(self.seccion_consulta_simple, text='Botones consulta')
            seccion_botones_consulta.grid(row=0, column=1, padx=5, pady=5, sticky='NW')

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_consulta = ttk.Button(seccion_botones_consulta, text='Realizar consulta', command=self.consulta_entrada)

            boton_consulta.grid(row=0, column=0, padx=5, pady=5)

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_limpiar_campos = ttk.Button(seccion_botones_consulta,  text='Limpiar campos', command = self.vaciar_campos)
            boton_limpiar_campos.grid(row=1, column=0, padx=5, pady=5)

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_limpiar_campos = ttk.Button(seccion_botones_consulta,  text='Vaciar tabla', command = self.vaciar_tabla)
            boton_limpiar_campos.grid(row=2, column=0, padx=5, pady=5)


        #Labelframe para consultas avanzadas
        self.seccion_consulta_avanzada = ttk.LabelFrame(self.seccion_formulario_datos, text='Consulta avanzada')

        def view_consulta_avanzada(self):

            seccion_fechas = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Fechas')
            seccion_fechas.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)


            ##########################################################################################################
            #####################################################
            # Crear un LabelFrame para las entradas
            seccion_entrada = ttk.LabelFrame(seccion_fechas, text='Entradas')
            seccion_entrada.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')


            # Crear el boton para el calendario entrada inicio
            boton_calendario_inicio_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, 
                                                    command=lambda: self.controlador_entrada.actualizar_fecha(
                                                                                            calendario=self.calendario_fecha_inicio_entrada,
                                                                                            fecha=self.fecha_hora_inicio_entrada,
                                                                                            variable=self.variable_fecha_inicio_entrada,
                                                                                            campo_texto=self.campo_texto_entrada_fecha_inicio))
            boton_calendario_inicio_entrada.grid(row=0, column=0, pady=5, sticky=tk.W)
            boton_calendario_inicio_entrada.grid(row=0, column=0, pady=5, sticky=tk.W)

            # Crear las leyendas para los campos de texto de las entradas
            etiqueta_fecha_inicio_entrada = ttk.Label(seccion_entrada, text='Fecha mayor a:', width=14)
            etiqueta_fecha_inicio_entrada.grid(row=0, column=1, pady=5, sticky=tk.W)
        
            # Crear los campos de texto para las entradas
            self.campo_texto_entrada_fecha_inicio = ttk.Label(seccion_entrada, text='', width=19)
            self.campo_texto_entrada_fecha_fin = ttk.Label(seccion_entrada, text='')


            # Crear el boton para el calendario entrada fin
            boton_calendario_fin_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, 
                                                    command=lambda:self.controlador_entrada.actualizar_fecha(
                                                                                            calendario=self.calendario_fecha_fin_entrada,
                                                                                            fecha=self.fecha_hora_fin_entrada,
                                                                                            variable=self.variable_fecha_fin_entrada,
                                                                                            campo_texto=self.campo_texto_entrada_fecha_fin))

            boton_calendario_fin_entrada.grid(row=1, column=0, pady=5, sticky=tk.W)

            etiqueta_fecha_fin_entrada = ttk.Label(seccion_entrada, text='Fecha menor a:', width=14)
            etiqueta_fecha_fin_entrada.grid(row=1, column=1, pady=5, sticky=tk.W)

            # Empaqueta los campos de texto y las leyendas en el LabelFrame de las entradas
            self.campo_texto_entrada_fecha_inicio.grid(row=0, column=2, pady=5,sticky=tk.W)
            self.campo_texto_entrada_fecha_fin.grid(row=1, column=2, pady=5, sticky=tk.W)
            #####################################################

            #####################################################
            # Crear un LabelFrame para las salidas
            seccion_salida = ttk.LabelFrame(seccion_fechas, text='Salidas')
            seccion_salida.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')

            # Crear el boton para el calendario salida inicio
            boton_calendario_inicio_salida = ttk.Button(seccion_salida, image=self.icono_calendario, 
                                                    command=lambda: self.controlador_entrada.actualizar_fecha(
                                                                                            calendario=self.calendario_fecha_inicio_salida,
                                                                                            fecha=self.fecha_hora_inicio_salida,
                                                                                            variable=self.variable_fecha_inicio_salida,
                                                                                            campo_texto=self.campo_texto_salida_fecha_inicio))
            boton_calendario_inicio_salida.grid(row=0, column=0, sticky=tk.W)

            # Crear los campos de texto para las salidas
            self.campo_texto_salida_fecha_inicio = ttk.Label(seccion_salida, text='')
            self.campo_texto_salida_fecha_fin = ttk.Label(seccion_salida, text='')

            # Crear las leyendas para los campos de texto de las salidas
            etiqueta_fecha_inicio_salida = ttk.Label(seccion_salida, text='Fecha mayor a:', width=14)
            etiqueta_fecha_inicio_salida.grid(row=0, column=1, pady=5, sticky=tk.W)


            # Crear el boton para el calendario salida fin
            boton_calendario_fin_salida = ttk.Button(seccion_salida, image=self.icono_calendario, 
                                                    command=lambda: self.controlador_entrada.actualizar_fecha(
                                                                                            calendario=self.calendario_fecha_fin_salida,
                                                                                            fecha=self.fecha_hora_fin_salida,
                                                                                            variable=self.variable_fecha_fin_salida,
                                                                                            campo_texto=self.campo_texto_salida_fecha_fin))
            
            boton_calendario_fin_salida.grid(row=1, column=0, sticky=tk.W)

            etiqueta_fecha_fin_salida = ttk.Label(seccion_salida, text='Fecha menor a:', width=14)
            etiqueta_fecha_fin_salida.grid(row=1, column=1, pady=5, sticky=tk.W)

            # Empaqueta los campos de texto y las leyendas en el LabelFrame de las salidas
            self.campo_texto_salida_fecha_inicio.grid(row=0, column=2, pady=5, sticky=tk.W)
            self.campo_texto_salida_fecha_fin.grid(row=1, column=2, pady=5, sticky=tk.W)
            ##########################################################################################################


            ##########################################################################################################
            seccion_tiempo_dentro = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Tiempo dentro')
            seccion_tiempo_dentro.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NW)

            opciones_minutos = [0, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
            opciones_horas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

            etiqueta_tiempo_dentro_hora = ttk.Label(seccion_tiempo_dentro,  text='Hrs')
            etiqueta_tiempo_dentro_hora.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NW)
            etiqueta_tiempo_dentro_min = ttk.Label(seccion_tiempo_dentro,  text='Min')
            etiqueta_tiempo_dentro_min.grid(row=0, column=2, padx=5 , pady=5, sticky=tk.NW)
            #####################################################
            self.variable_tiempo_dentro_hora = IntVar()
            self.variable_tiempo_dentro_minuto = IntVar()

            etiqueta_tiempo_dentro_hora = ttk.Label(seccion_tiempo_dentro,  text='Tiempo: ')
            etiqueta_tiempo_dentro_hora.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

            self.lista_desplegable_tiempo_dentro_hora = ttk.Combobox(seccion_tiempo_dentro, values=opciones_horas, textvariable=self.variable_tiempo_dentro_hora, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_hora.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_hora.configure(foreground="black")

            self.lista_desplegable_tiempo_dentro_minuto = ttk.Combobox(seccion_tiempo_dentro, values=opciones_minutos, textvariable=self.variable_tiempo_dentro_minuto, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_minuto.grid(row=1, column=2, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_minuto.configure(foreground="black")
            #####################################################

            #####################################################
            self.variable_tiempo_dentro_hora_inicio = IntVar()
            self.variable_tiempo_dentro_minuto_inicio = IntVar()

            etiqueta_hora = ttk.Label(seccion_tiempo_dentro, text="Tiempo mayor a: ")
            etiqueta_hora.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)

            self.lista_desplegable_tiempo_dentro_hora_inicio = ttk.Combobox(seccion_tiempo_dentro, values=opciones_horas, textvariable=self.variable_tiempo_dentro_hora_inicio, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_hora_inicio.grid(row=2, column=1, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_hora_inicio.configure(foreground="black")

            self.lista_desplegable_tiempo_dentro_minuto_inicio = ttk.Combobox(seccion_tiempo_dentro, values=opciones_minutos, textvariable=self.variable_tiempo_dentro_minuto_inicio, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_minuto_inicio.grid(row=2, column=2, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_minuto_inicio.configure(foreground="black")
            #####################################################

            #####################################################
            self.variable_tiempo_dentro_hora_fin = IntVar()
            self.variable_tiempo_dentro_minuto_fin = IntVar()

            etiqueta_hora = ttk.Label(seccion_tiempo_dentro, text="Tiempo menor a: ")
            etiqueta_hora.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)

            self.lista_desplegable_tiempo_dentro_hora_fin = ttk.Combobox(seccion_tiempo_dentro, values=opciones_horas, textvariable=self.variable_tiempo_dentro_hora_fin, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_hora_fin.grid(row=3, column=1, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_hora_fin.configure(foreground="black")

            self.lista_desplegable_tiempo_dentro_minuto_fin = ttk.Combobox(seccion_tiempo_dentro, values=opciones_minutos, textvariable=self.variable_tiempo_dentro_minuto_fin, state='readonly',width=3 ,height=5)
            self.lista_desplegable_tiempo_dentro_minuto_fin.grid(row=3, column=2, padx=5, pady=5, sticky=tk.NW)
            self.lista_desplegable_tiempo_dentro_minuto_fin.configure(foreground="black")
            #####################################################
            ##########################################################################################################


            ##########################################################################################################
            seccion_tarifas = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Tarifas')
            seccion_tarifas.grid(row=0, column=2, padx=5, pady=5, sticky=tk.NW)
            
            self.lista_tarifa_preferente = tk.Listbox(seccion_tarifas, selectmode="multiple", height=5)
            self.lista_tarifa_preferente.grid(row=0, column=0, sticky="nsew")

            scrollbar = ttk.Scrollbar(seccion_tarifas, orient="vertical", command=self.lista_tarifa_preferente.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")
            self.lista_tarifa_preferente.configure(yscrollcommand=scrollbar.set)

            seccion_tarifas.rowconfigure(0, weight=1)
            seccion_tarifas.columnconfigure(0, weight=1)

            promociones = self.query.obtener_lista_de('TarifaPreferente')
            for promocion in promociones:
                self.lista_tarifa_preferente.insert(tk.END, promocion)
            ##########################################################################################################


            ##########################################################################################################
            seccion_cortes = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Cortes')
            seccion_cortes.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)


            opciones = self.query.obtener_lista_de('CorteInc', 'D')


            etiqueta_corte = ttk.Label(seccion_cortes,  text='Corte: ')
            etiqueta_corte.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_corte = ttk.Combobox(seccion_cortes,  values=opciones, textvariable=self.variable_corte_numero, state='readonly', height=5)
            self.lista_desplegable_corte.grid(row=0, column=1, padx=5, pady=5)

            etiqueta_corte_inicio = ttk.Label(seccion_cortes,  text='Corte mayor a: ')
            etiqueta_corte_inicio.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_corte_inicio = ttk.Combobox(seccion_cortes,  values=opciones, textvariable=self.variable_corte_inicio, state='readonly', height=5)
            self.lista_desplegable_corte_inicio.grid(row=1, column=1, padx=5, pady=5)

            etiqueta_corte_final = ttk.Label(seccion_cortes,  text='Corte menor a: ')
            etiqueta_corte_final.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_corte_final = ttk.Combobox(seccion_cortes,  values=opciones, textvariable=self.variable_corte_fin, state='readonly', height=5)
            self.lista_desplegable_corte_final.grid(row=2, column=1, padx=5, pady=5)
            ##########################################################################################################

            ##########################################################################################################
            seccion_importe = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Importe')
            seccion_importe.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NW)


            opciones = self.query.obtener_lista_de('Importe', 'A')


            etiqueta_importe = ttk.Label(seccion_importe,  text='Importe: ')
            etiqueta_importe.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_ingreso = ttk.Combobox(seccion_importe,  values=opciones, textvariable=self.variable_importe, state='readonly', height=5)
            self.lista_desplegable_ingreso.grid(row=0, column=1, padx=5, pady=5)

            etiqueta_importe_inicio = ttk.Label(seccion_importe,  text='Importe mayor a: ')
            etiqueta_importe_inicio.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_ingreso_inicio = ttk.Combobox(seccion_importe,  values=opciones, textvariable=self.variable_importe_inicio, state='readonly', height=5)
            self.lista_desplegable_ingreso_inicio.grid(row=1, column=1, padx=5, pady=5)

            etiqueta_importe_final = ttk.Label(seccion_importe,  text='Importe menor a: ')
            etiqueta_importe_final.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
            self.lista_desplegable_ingreso_final = ttk.Combobox(seccion_importe,  values=opciones, textvariable=self.variable_importe_final, state='readonly', height=5)
            self.lista_desplegable_ingreso_final.grid(row=2, column=1, padx=5, pady=5)
            ##########################################################################################################

            ##########################################################################################################
            seccion_promociones = ttk.LabelFrame(self.seccion_consulta_avanzada, text='Promociones')
            seccion_promociones.grid(row=0, column=3, padx=5, pady=5, sticky=tk.NW)


            self.lista_promociones = tk.Listbox(seccion_promociones, selectmode="multiple", height=5)
            self.lista_promociones.grid(row=0, column=0, sticky="nsew")

            scrollbar = ttk.Scrollbar(seccion_promociones, orient="vertical", command=self.lista_promociones.yview)
            scrollbar.grid(row=0, column=1, sticky="ns")
            self.lista_promociones.configure(yscrollcommand=scrollbar.set)

            seccion_promociones.rowconfigure(0, weight=1)
            seccion_promociones.columnconfigure(0, weight=1)

            promociones = self.query.obtener_lista_de('TipoPromocion')
            #promociones = self.query.obtener_lista_de('TarifaPreferente')
            for promocion in promociones:
                self.lista_promociones.insert(tk.END, promocion)
            ##########################################################################################################

            ##########################################################################################################
            # Crea un LabelFrame para los botones de desconectar y salir
            seccion_botones_consulta = ttk.LabelFrame(self.seccion_consulta_avanzada , text='Botones consulta')
            seccion_botones_consulta.grid(row=1, column=3, padx=5, pady=5, sticky=tk.NW)

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_consulta = ttk.Button(seccion_botones_consulta, text='Realizar consulta', command=self.consulta_entrada, width=16)
            boton_consulta.grid(row=0, column=0, padx=5, pady=5)

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_limpiar_campos = ttk.Button(seccion_botones_consulta,  text='Limpiar campos', command = self.vaciar_campos, width=16)
            boton_limpiar_campos.grid(row=1, column=0, padx=5, pady=5)

            # Crea un botón y lo empaqueta en la seccion_botones_consulta
            boton_limpiar_campos = ttk.Button(seccion_botones_consulta,  text='Vaciar tabla', command = self.limpiar_registros, width=16)
            boton_limpiar_campos.grid(row=2, column=0, padx=5, pady=5)
            ##########################################################################################################


        view_consulta_simple(self)
        view_consulta_avanzada(self)

    def view_tabla(self):
        """
        Crea una tabla en la interfaz y la llena con los datos de la base de datos.

        Esta función utiliza el método `obtener_campos_tabla` de la instancia de la clase `query`
        para obtener los nombres de las columnas de la tabla que se va a mostrar en la interfaz.
        Luego, crea un `Treeview` con una columna por cada campo de la tabla, configura los encabezados
        de las columnas y los tamaños de columna. Finalmente, inserta los datos en el `Treeview`.
        """
        # Crea un Frame para la tabla y lo configura para llenar todo el espacio disponible

        seccion_tabla = ttk.LabelFrame(self.panel, text = '')
        seccion_tabla.columnconfigure(0, weight=1, uniform='tabla')
        seccion_tabla.rowconfigure(0, weight=1)
        seccion_tabla.grid_propagate(True)
        seccion_tabla.grid(row=1, column=0, sticky='nsew') 


        # Obtiene los nombres de las columnas de la tabla que se va a mostrar
        columnas = self.query.obtener_campos_tabla()

        # Crea un Treeview con una columna por cada campo de la tabla
        self.tabla = ttk.Treeview(seccion_tabla, columns=(columnas))
        self.tabla.config(height=15)

        # Define los encabezados de columna
        i = 1
        for headd in (columnas):
            self.tabla.heading(f'#{i}', text=headd)
            self.tabla.column(f'#{i}', width=100)
            i = i + 1
        self.tabla.column('#0', width=0, stretch=False)
        self.tabla.column('#1', width=40, stretch=False)

        # Inserta datos
        #self.ver_tabla_completa()

        # Crea un Scrollbar vertical y lo asocia con el Treeview
        scrollbar_Y = ttk.Scrollbar(seccion_tabla, orient='vertical', command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar_Y.set)
        scrollbar_Y.grid(row=0, column=1, sticky='NS')

        # Crea un Scrollbar horizontal y lo asocia con el Treeview
        scrollbar_X = ttk.Scrollbar(seccion_tabla, orient='horizontal', command=self.tabla.xview)
        self.tabla.configure(xscroll=scrollbar_X.set)
        scrollbar_X.grid(row=1, column=0, sticky='EW')

        # Empaqueta el Treeview en la ventana
        self.tabla.grid(row=0, column=0, sticky='NESW', padx=5, pady=5, ipadx=5, ipady=5, columnspan=2, rowspan=2)



    def mostrar_campos_simple(self):
        """
        Muestra los campos de entrada de la consulta simple en la interfaz gráfica.

        Esta función se encarga de mostrar los campos de entrada de la consulta simple en la interfaz gráfica,
        y ocultar la sección de consulta avanzada y la sección de formulario de datos si es que están visibles.
        Además, llama a la función "vaciar_campos()" para limpiar los campos de entrada de texto y variables
        de control en la interfaz gráfica.
        """
        if self.seccion_formulario_datos.winfo_ismapped():
            self.seccion_consulta_simple.grid_forget()  # ocultar el labelframe
            self.seccion_consulta_avanzada.grid_forget()
            self.seccion_formulario_datos.grid_forget()
            self.vaciar_campos()
        else:
            self.seccion_consulta_avanzada.grid_forget()
            self.seccion_consulta_simple.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')  # mostrar el labelframe 
            self.seccion_formulario_datos.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

    def mostrar_campos_avanzado(self):
        """
        Muestra los campos de entrada de la consulta avanzada en la interfaz gráfica.

        Esta función se encarga de mostrar los campos de entrada de la consulta avanzada en la interfaz gráfica,
        y ocultar la sección de consulta simple y la sección de formulario de datos si es que están visibles.
        Además, llama a la función "vaciar_campos()" para limpiar los campos de entrada de texto y variables
        de control en la interfaz gráfica.
        """
        if self.seccion_formulario_datos.winfo_ismapped():
            self.seccion_consulta_simple.grid_forget()  # ocultar el labelframe
            self.seccion_consulta_avanzada.grid_forget()
            self.seccion_formulario_datos.grid_forget()
            self.vaciar_campos()
        else:
            self.seccion_consulta_simple.grid_forget()
            self.seccion_consulta_avanzada.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')  # mostrar el labelframe 
            self.seccion_formulario_datos.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)



    def ver_tabla_completa(self):
        '''Método para visualizar la tabla completa sin restricciones.'''
        #Advierte sobre la cantidad de registros
        if messagebox.askokcancel(title='Advertencia',message='Al ver todos los registros de la tabla, debe considerar que para reaizar esta consulta el tiempo de respuesta puede variar desde unos segundos hasta minutos, pasaria lo mismo si quiere realizar un reporte de esta consulta.\n\n ¿Quiere continuar?'):
            # Obtiene todos los registros
            self.registros = self.query.obtener_registros_completos()
            
            # Llena la tabla con los registros
            self.llenar_tabla(self.registros)

    def llenar_tabla(self, registros):
        '''Llena la tabla con los registros que cumplen con los criterios de búsqueda.

        Parameters:
        registros: list
            Una lista de tuplas que representan los registros obtenidos de la base de datos.
        '''
        # Limpia la tabla antes de llenarla con nuevos registros
        self.vaciar_tabla()

        if self.registros:
            for registro in registros:
                self.tabla.insert('', 'end', values=registro)

    def vaciar_tabla(self):
        """
        Elimina todas las filas de la tabla.
        """
        # Elimina todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())

    def limpiar_registros(self):
        '''
        Elimina todos los registros de la variable registros y vacia la tabla
        '''

        self.registros = None
        self.parametros = ''
        self.vaciar_tabla()

    def vaciar_campos(self):
        """
        Limpia los campos de entrada de texto y variables de control en la interfaz gráfica.

        Esta función se encarga de limpiar los campos de entrada de texto y variables de control en la interfaz gráfica.
        """
        self.variable_folio.set('')

        self.variable_tarifa_preferente.set('')
        self.variable_tipo_tarifa_preferente = ''


        self.variable_fecha_inicio_entrada.set('')
        self.variable_fecha_fin_entrada.set('')
        self.variable_fecha_inicio_salida.set('')
        self.variable_fecha_fin_salida.set('')


        self.variable_tiempo_dentro.set('')
        self.variable_tiempo_dentro_fin.set('')
        self.variable_tiempo_dentro_inicio.set('')

        self.variable_tiempo_dentro_hora.set('0')
        self.variable_tiempo_dentro_minuto.set('0')

        self.variable_tiempo_dentro_hora_inicio.set('0')
        self.variable_tiempo_dentro_minuto_inicio.set('0')

        self.variable_tiempo_dentro_hora_fin.set('0')
        self.variable_tiempo_dentro_minuto_fin.set('0')


        self.variable_tipo_promocion = ''
        self.variable_promocion.set('')

        self.variable_corte_numero.set('')
        self.variable_corte_inicio.set('')
        self.variable_corte_fin.set('')


        self.variable_importe.set('')
        self.variable_importe_final.set('')
        self.variable_importe_inicio.set('')




        # Limpia los campos de consulta
        self.campo_texto_folio.delete(0, 'end')

        self.lista_desplegable_tipo_tarifa_preferente.selection_clear()
        self.lista_tarifa_preferente.selection_clear(0, 'end')


        self.campo_texto_entrada_fecha_inicio.config(text="")
        self.campo_texto_entrada_fecha_fin.config(text="")

        self.campo_texto_salida_fecha_fin.config(text="")
        self.campo_texto_salida_fecha_inicio.config(text="")


        self.lista_desplegable_tiempo_dentro_hora.selection_clear()
        self.lista_desplegable_tiempo_dentro_minuto.selection_clear()

        self.lista_desplegable_tiempo_dentro_hora_inicio.selection_clear()
        self.lista_desplegable_tiempo_dentro_minuto_inicio.selection_clear()

        self.lista_desplegable_tiempo_dentro_hora_fin.selection_clear()
        self.lista_desplegable_tiempo_dentro_minuto_fin.selection_clear()


        self.lista_promociones.selection_clear(0, 'end')
        self.lista_desplegable_tipo_promocion.selection_clear()


        self.lista_desplegable_corte.selection_clear()
        self.lista_desplegable_corte_inicio.selection_clear()
        self.lista_desplegable_corte_final.selection_clear()


        self.lista_desplegable_ingreso.selection_clear()
        self.lista_desplegable_ingreso_inicio.selection_clear()
        self.lista_desplegable_ingreso_final.selection_clear()

    def obtener_variables(self):
        """
        Esta función se encarga de obtener las variables necesarias para crear un objeto de reserva
        a partir de los valores seleccionados por el usuario en la interfaz gráfica.

        La función utiliza widgets de tkinter para obtener los valores seleccionados por el usuario,
        y los almacena en variables que son utilizadas por otras funciones para crear el objeto de reserva.

        La función no toma argumentos, ya que utiliza variables de clase para almacenar los valores.

        """

        # Obtener los índices de los elementos seleccionados en la lista de tarifa preferente
        indices_seleccionados = self.lista_tarifa_preferente.curselection()
        # Obtener los valores correspondientes a los índices seleccionados
        (self.variable_tipo_tarifa_preferente) = [self.lista_tarifa_preferente.get(i) for i in indices_seleccionados]

        # Obtener los índices de los elementos seleccionados en la lista de promociones
        indices_seleccionados = self.lista_promociones.curselection()
        # Obtener los valores correspondientes a los índices seleccionados
        (self.variable_tipo_promocion) = [self.lista_promociones.get(i) for i in indices_seleccionados]

        # Obtener el tiempo dentro en formato HH:MM:SS
        self.variable_tiempo_dentro.set(f'{int(self.variable_tiempo_dentro_hora.get())}'+':'+f'{int(self.variable_tiempo_dentro_minuto.get())}'+':00')

        # Obtener la hora de inicio del tiempo dentro en formato HH:MM:SS
        self.variable_tiempo_dentro_inicio.set(f'{int(self.variable_tiempo_dentro_hora_inicio.get())}'+':'+f'{int(self.variable_tiempo_dentro_minuto_inicio.get())}'+':00')

        # Obtener la hora de finalización del tiempo dentro en formato HH:MM:SS
        self.variable_tiempo_dentro_fin.set(f'{int(self.variable_tiempo_dentro_hora_fin.get())}'+':'+f'{int(self.variable_tiempo_dentro_minuto_fin.get())}'+':00')


    def consulta_entrada(self):
            """
            Realiza una consulta de entrada con los parámetros proporcionados por el usuario y llena la tabla con los resultados obtenidos.
            """
            self.obtener_variables()

            # Se llama a la función de hacer_consulta_entrada del controlador de entrada para obtener los registros correspondientes
            self.registros, self.parametros = self.controlador_entrada.hacer_consulta_entrada(
                                                                                id = self.variable_folio.get(),
                                                                                tarifa_preferente = self.variable_tipo_tarifa_preferente,
                                                                                tarifa = self.variable_tarifa_preferente.get(),


                                                                                tipo_promocion = self.variable_tipo_promocion,
                                                                                promocion = self.variable_promocion.get(),


                                                                                fecha_inicio_entrada = self.variable_fecha_inicio_entrada.get(),
                                                                                fecha_fin_entrada = self.variable_fecha_fin_entrada.get(),
                                                                                fecha_inicio_salida = self.variable_fecha_inicio_salida.get(),
                                                                                fecha_fin_salida = self.variable_fecha_fin_salida.get(),

                                                                                tiempo_dentro = self.variable_tiempo_dentro.get(),
                                                                                tiempo_dentro_inicio = self.variable_tiempo_dentro_inicio.get(),
                                                                                tiempo_dentro_fin = self.variable_tiempo_dentro_fin.get(),
                                                                            

                                                                                corte_numero = self.variable_corte_numero.get(),
                                                                                corte_numero_inicio = self.variable_corte_inicio.get(),
                                                                                corte_numero_fin = self.variable_corte_fin.get(),

                                                                                ingreso = self.variable_importe.get(),
                                                                                ingreso_mayor = self.variable_importe_final.get(),
                                                                                ingreso_menor = self.variable_importe_inicio.get())

            # Se llena la tabla con los registros obtenidos
            self.llenar_tabla(self.registros)


    def desconectar(self):
        pass

    def salir(self):
        """
        Muestra un cuadro de diálogo para informar al usuario que se está cerrando la aplicación y destruye el panel principal.
        """
        #vaciar los campos antes de salir
        self.vaciar_campos()
        #vaciar la tabla antes de salir
        self.vaciar_tabla()

        # Muestra un cuadro de diálogo con el mensaje "Hasta pronto"
        messagebox.showinfo('Salida', 'Hasta pronto.')
        
        #detener el loop principal
        self.panel.quit()
        # Destruye el panel principal
        self.panel.destroy()

