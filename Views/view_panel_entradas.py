import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import PhotoImage
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


        # Establece el tamaño de la ventana y su título
        self.panel.geometry()
        #self.panel.resizable(False, False)

        self.panel.title(f'Panel de administración reporte general - Cortes')


        # Configura la columna principal del panel para que use todo el espacio disponible
        self.panel.columnconfigure(0, weight=1)


        # Crea las variables para los campos de consulta
        self.variable_corte_numero = StringVar()
        self.variable_folio = StringVar()
        self.variable_tarifa_preferente = StringVar()
        self.variable_tipo_promocion = StringVar()


        self.variable_fecha_inicio_entrada = StringVar()
        self.variable_fecha_fin_entrada = StringVar()
        self.variable_fecha_inicio_salida = StringVar()
        self.variable_fecha_fin_salida = StringVar()


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
        self.icono_salir = PhotoImage(file=icono_salir).subsample(25)

        icono_desconectar = tools_instance.read_path_config_file('images', 'icono_desconectar')
        self.icono_desconectar = PhotoImage(file=icono_desconectar).subsample(25)


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
        self.query = Queries()
        self.message = None
        self.tabla = None


        # Crea la tabla y los campos de consulta
        self.view_tabla()
        self.view_campos_consulta()


        self.controlador_entrada = EntradasController(self.theme)


        # Inicia el loop principal de la ventana
        self.panel.mainloop()


    def view_campos_consulta(self):
        '''Crea y empaqueta los campos de consulta en la ventana.'''

        seccion_principal = ttk.LabelFrame(self.panel, text='')
        seccion_principal.columnconfigure(1, weight=1)
        seccion_principal.grid_propagate(True)
        seccion_principal.grid(row=0, column=0, sticky=tk.NSEW)


        seccion_logo = ttk.LabelFrame(seccion_principal, text='')
        seccion_logo.grid(row=0, column=0, sticky=tk.NW)

        etiqueta_logo = tk.Label(seccion_logo, image=self.logo_pase)
        etiqueta_logo.grid(row=0, column=0, sticky=tk.NW)


        seccion_menu_consulta = ttk.LabelFrame(seccion_principal, text='Selecciona tipo de consulta', padding=10)
        seccion_menu_consulta.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        boton_campos_simple = ttk.Button(seccion_menu_consulta, text='Consulta simple', command=self.mostrar_campos_simple)
        boton_campos_simple.grid(row=0, column=0, sticky='')

        boton_ver_todo = ttk.Button(seccion_menu_consulta, text='Consulta avanzado')
        boton_ver_todo.grid(row=0, column=1, sticky='')

        # Configurar las columnas intermedias con un tamaño mínimo
        seccion_menu_consulta.columnconfigure(2, minsize=50)
        seccion_menu_consulta.columnconfigure(3, minsize=50)

        boton_generar_reporte = ttk.Button(seccion_menu_consulta, text='Generar reporte', width=15,
        command = lambda:
                        {
                            self.controlador_entrada.realizar_reporte(registros = self.registros),
                            self.vaciar_campos()
                        })
        boton_generar_reporte.grid(row=0, column=4, pady=5)


        self.seccion_formulario_datos = ttk.LabelFrame(seccion_principal, text='Ingresa los datos de la consulta', padding=10)



        # Crear un LabelFrame para la consulta de corte y folio
        self.seccion_consulta = ttk.LabelFrame(self.seccion_formulario_datos, text='Consulta simple')

        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de folio
        etiqueta_folio = ttk.Label(self.seccion_consulta, text='N° de boleto: ')
        etiqueta_folio.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto para la consulta de folio
        self.campo_texto_folio = tk.Entry(self.seccion_consulta, textvariable=self.variable_folio)
        self.campo_texto_folio.grid(row=0, column=1, padx=5, pady=5)
        #######################################################################---

        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de corte
        etiqueta_corte = ttk.Label(self.seccion_consulta, text='N° de corte: ')
        etiqueta_corte.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto para la consulta de corte
        self.campo_texto_corte = tk.Entry(self.seccion_consulta, textvariable=self.variable_corte_numero)
        self.campo_texto_corte.grid(row=1, column=1, padx=5, pady=5)
        #######################################################################---

        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de corte
        etiqueta_tipo_tarifa = ttk.Label(self.seccion_consulta, text='Tipo de tarifa: ')
        etiqueta_tipo_tarifa.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)


        opciones = self.query.obtener_lista_de('TarifaPreferente')
        # Crear la lista desplegable
        self.lista_desplegable_tipo_tarifa = ttk.Combobox(self.seccion_consulta, values=opciones, textvariable=self.variable_tarifa_preferente, state='readonly')
        self.lista_desplegable_tipo_tarifa.grid(row=2, column=1, padx=5, pady=5)
        #######################################################################---


        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de corte
        etiqueta_tipo_promocion = ttk.Label(self.seccion_consulta, text='Tipo de promoción: ')
        etiqueta_tipo_promocion.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)


        opciones = self.query.obtener_lista_de('TipoPromocion')
        # Crear la lista desplegable
        self.lista_desplegable_tipo_promocion = ttk.Combobox(self.seccion_consulta, values=opciones, textvariable=self.variable_tipo_promocion, state='readonly')
        self.lista_desplegable_tipo_promocion.grid(row=3, column=1, padx=5, pady=5)



        # # Crear los campos de texto para la consulta de corte
        # self.campo_texto_tipo_promocion = tk.Entry(self.seccion_consulta, textvariable=self.variable_tipo_promocion)
        # self.campo_texto_tipo_promocion.grid(row=3, column=1, padx=5, pady=5)
        #######################################################################---




        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_consulta = ttk.Button(self.seccion_consulta, text='Limpiar campos', command = self.vaciar_campos, width=15)
        boton_consulta.grid(row=4, column=0, pady=5)



        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_consulta = ttk.Button(self.seccion_consulta, text='Realizar consulta', command = self.hacer_consulta_entrada, width=15)
        boton_consulta.grid(row=4, column=1, pady=5)


        # #######################################################################---
        # # Crear un LabelFrame para las entradas
        # seccion_entrada = ttk.LabelFrame(seccion_principal, text='Entradas')
        # seccion_entrada.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')



        # # Crear el boton para el calendario entrada inicio
        # boton_calendario_inicio_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, 
        #                                         command=lambda: self.controlador_entrada.actualizar_fecha(
        #                                                                                 calendario=self.calendario_fecha_inicio_entrada,
        #                                                                                 fecha=self.fecha_hora_inicio_entrada,
        #                                                                                 variable=self.variable_fecha_inicio_entrada,
        #                                                                                 campo_texto=self.campo_texto_entrada_fecha_inicio))
        # boton_calendario_inicio_entrada.grid(row=0, column=0, sticky=tk.W)

        # # Crear las leyendas para los campos de texto de las entradas
        # etiqueta_fecha_inicio_entrada = ttk.Label(seccion_entrada, text='Fecha inicio:', width=12, anchor=tk.W)
        # etiqueta_fecha_inicio_entrada.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
       
        # # Crear los campos de texto para las entradas
        # self.campo_texto_entrada_fecha_inicio = ttk.Label(seccion_entrada, text='')
        # self.campo_texto_entrada_fecha_fin = ttk.Label(seccion_entrada, text='')



        # # Crear el boton para el calendario entrada fin
        # boton_calendario_fin_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, 
        #                                         command=lambda:self.controlador_entrada.actualizar_fecha(
        #                                                                                 calendario=self.calendario_fecha_fin_entrada,
        #                                                                                 fecha=self.fecha_hora_fin_entrada,
        #                                                                                 variable=self.variable_fecha_fin_entrada,
        #                                                                                 campo_texto=self.campo_texto_entrada_fecha_fin))

        # boton_calendario_fin_entrada.grid(row=1, column=0, sticky=tk.W)

        # etiqueta_fecha_fin_entrada = ttk.Label(seccion_entrada, text='Fecha fin:')
        # etiqueta_fecha_fin_entrada.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # # Empaqueta los campos de texto y las leyendas en el LabelFrame de las entradas
        # self.campo_texto_entrada_fecha_inicio.grid(row=0, column=2, padx=5, pady=5,sticky='nsew')
        # self.campo_texto_entrada_fecha_fin.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        # #######################################################################---





        # #######################################################################---
        # # Crear un LabelFrame para las salidas
        # seccion_salida = ttk.LabelFrame(seccion_principal, text='Salidas')
        # seccion_salida.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')



        # # Crear el boton para el calendario salida inicio
        # boton_calendario_inicio_salida = ttk.Button(seccion_salida, image=self.icono_calendario, 
        #                                         command=lambda: self.controlador_entrada.actualizar_fecha(
        #                                                                                 calendario=self.calendario_fecha_inicio_salida,
        #                                                                                 fecha=self.fecha_hora_inicio_salida,
        #                                                                                 variable=self.variable_fecha_inicio_salida,
        #                                                                                 campo_texto=self.campo_texto_salida_fecha_inicio))
        # boton_calendario_inicio_salida.grid(row=0, column=0, sticky=tk.W)


        # # Crear los campos de texto para las salidas
        # self.campo_texto_salida_fecha_inicio = ttk.Label(seccion_salida, text='')
        # self.campo_texto_salida_fecha_fin = ttk.Label(seccion_salida, text='')

        # # Crear las leyendas para los campos de texto de las salidas
        # etiqueta_fecha_inicio_salida = ttk.Label(seccion_salida, text='Fecha inicio:')
        # etiqueta_fecha_inicio_salida.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)




        # # Crear el boton para el calendario salida fin
        # boton_calendario_fin_salida = ttk.Button(seccion_salida, image=self.icono_calendario, 
        #                                         command=lambda: self.controlador_entrada.actualizar_fecha(
        #                                                                                 calendario=self.calendario_fecha_fin_salida,
        #                                                                                 fecha=self.fecha_hora_fin_salida,
        #                                                                                 variable=self.variable_fecha_fin_salida,
        #                                                                                 campo_texto=self.campo_texto_salida_fecha_fin))
        
        # boton_calendario_fin_salida.grid(row=1, column=0, sticky=tk.W)

        # etiqueta_fecha_fin_salida = ttk.Label(seccion_salida, text='Fecha fin:')
        # etiqueta_fecha_fin_salida.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # # Empaqueta los campos de texto y las leyendas en el LabelFrame de las salidas
        # self.campo_texto_salida_fecha_inicio.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        # self.campo_texto_salida_fecha_fin.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        # #######################################################################---




        # #######################################################################---
        # # Crea un LabelFrame para los botones de consulta
        # seccion_botones_consulta = ttk.LabelFrame(seccion_principal, text='Consulta')
        # seccion_botones_consulta.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')




        # # Crea un botón y lo empaqueta en la seccion_botones_consulta
        # boton_generar_reporte = ttk.Button(seccion_botones_consulta, text='Generar reporte', width=15,
        # command = lambda:
        #                 {
        #                     self.controlador_entrada.realizar_reporte(registros = self.registros),
        #                     self.vaciar_campos()
        #                 })
        # boton_generar_reporte.grid(row=2, column=0, pady=5)




        # Crea un LabelFrame para los botones de desconectar y salir
        seccion_botones_salir = ttk.LabelFrame(seccion_principal, text='Salir')
        seccion_botones_salir.grid(row=0, column=3, padx=5, pady=5, sticky='NW')

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_desconectar = ttk.Button(seccion_botones_salir, text='Desconectar', command=self.desconectar,  image=self.icono_desconectar)
        boton_desconectar.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_salir = ttk.Button(seccion_botones_salir, text='Salir', command=self.salir, image=self.icono_salir)
        boton_salir.grid(row=0, column=1, pady=5)


    def view_tabla(self):
        """
        Crea una tabla en la interfaz y la llena con los datos de la base de datos.

        Esta función utiliza el método `obtener_campos_tabla` de la instancia de la clase `query`
        para obtener los nombres de las columnas de la tabla que se va a mostrar en la interfaz.
        Luego, crea un `Treeview` con una columna por cada campo de la tabla, configura los encabezados
        de las columnas y los tamaños de columna. Finalmente, inserta los datos en el `Treeview`.

        """
        # Crea un Frame para la tabla y lo configura para llenar todo el espacio disponible

        seccion_tabla = ttk.LabelFrame(self.panel, text=f'Tabla - {self.ver_tabla}')
        seccion_tabla.columnconfigure(0, weight=1, uniform='tabla')
        seccion_tabla.rowconfigure(0, weight=1)
        seccion_tabla.grid_propagate(True)
        seccion_tabla.grid(row=1, column=0, sticky='nsew')


        # Obtiene los nombres de las columnas de la tabla que se va a mostrar
        columnas = self.query.obtener_campos_tabla()

        # Crea un Treeview con una columna por cada campo de la tabla
        style = ttk.Style()

        #style.theme_use('xpnative')
        self.tabla = ttk.Treeview(seccion_tabla, columns=(columnas))
        self.tabla.config(height=15)

        # Define los encabezados de columna
        i = 1
        for headd in (columnas):
            self.tabla.heading(f'#{i}', text=headd)
            self.tabla.column(f'#{i}', width=100)
            i = i + 1
        self.tabla.column('#0', width=10, stretch=False)
        self.tabla.column('#1', width=50, stretch=False)

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
        self.tabla.grid(row=0, column=0, sticky='NESW')


    def mostrar_campos_simple(self):
        if self.seccion_formulario_datos.winfo_ismapped():
            self.seccion_consulta.grid_forget()  # ocultar el labelframe
            self.seccion_formulario_datos.grid_forget()
        else:
            self.seccion_consulta.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')  # mostrar el labelframe 
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

        # Itera a través de los registros y los inserta en la tabla
        for registro in registros:
            self.tabla.insert('', 'end', values=registro)


    def vaciar_tabla(self):
        """
        Elimina todas las filas de la tabla.
        """
        # Elimina todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())


    def vaciar_campos(self):
        """
        Limpia los campos de entrada de texto y variables de control en la interfaz gráfica.

        Esta función se encarga de limpiar los campos de entrada de texto y variables de control en la interfaz gráfica.
        En particular, los siguientes elementos son limpiados:
        - campo_texto_corte
        - campo_texto_folio
        - campo_texto_entrada_fecha_inicio
        - campo_texto_entrada_fecha_fin
        - campo_texto_salida_fecha_fin
        - campo_texto_salida_fecha_inicio
        - variable_corte_numero
        - variable_folio
        - variable_fecha_inicio_entrada
        - variable_fecha_fin_entrada
        - variable_fecha_inicio_salida
        - variable_fecha_fin_salida
        """
        # Limpia los campos de texto
        self.campo_texto_corte.delete(0, 'end')
        self.campo_texto_folio.delete(0, 'end')
        self.lista_desplegable_tipo_tarifa.selection_clear()
        self.lista_desplegable_tipo_tarifa.selection_clear()


        # self.campo_texto_entrada_fecha_inicio.config(text="")
        # self.campo_texto_entrada_fecha_fin.config(text="")

        # self.campo_texto_salida_fecha_fin.config(text="")
        # self.campo_texto_salida_fecha_inicio.config(text="")



        # Limpia las variables de control
        self.variable_corte_numero.set('')
        self.variable_folio.set('')
        self.variable_tarifa_preferente.set('')
        self.variable_tipo_promocion.set('')
        self.variable_fecha_inicio_entrada.set('')
        self.variable_fecha_fin_entrada.set('')
        self.variable_fecha_inicio_salida.set('')
        self.variable_fecha_fin_salida.set('')


    def hacer_consulta_entrada(self):
        """
        Realiza una consulta de entrada con los parámetros proporcionados por el usuario y llena la tabla con los resultados obtenidos.
        """
        self.registros = self.controlador_entrada.hacer_consulta_entrada(
                                                                        corte_numero = self.variable_corte_numero.get(),
                                                                        id = self.variable_folio.get(),
                                                                        tarifa_preferente = self.variable_tarifa_preferente.get(),
                                                                        tipo_promocion = self.variable_tipo_promocion.get(),
                                                                        fecha_inicio_entrada = self.variable_fecha_inicio_entrada.get(),
                                                                        fecha_fin_entrada = self.variable_fecha_fin_entrada.get(),
                                                                        fecha_inicio_salida = self.variable_fecha_inicio_salida.get(),
                                                                        fecha_fin_salida = self.variable_fecha_fin_salida.get())
        if self.registros:
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

