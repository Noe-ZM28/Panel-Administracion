import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import TclError
from tkinter import filedialog
from tkinter import StringVar
from tkinter import PhotoImage

from Config.config_tools import tools
from Models.queries import Queries
from Views.views_tools import Fecha_Hora

import threading

import xlsxwriter
from xlsxwriter import exceptions

from datetime import datetime

from ttkthemes import ThemedStyle




class Panel_Entradas:
    '''Clase principal que maneja la interfaz gráfica del usuario.'''

    def __init__(self):
        '''
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.
        '''

        # Establece la tabla que se visualizará por defecto
        self.ver_tabla = 'Entradas'

        # Crea la ventana principal
        self.panel = tk.Tk()

        #temas xd
        style = ThemedStyle(self.panel)
        #style.theme_use('aquativo')
        #style.theme_use('arc')
        #style.theme_use('black')
        #style.theme_use('blue')
        #style.theme_use('breeze')
        #style.theme_use('clearlooks')
        #style.theme_use('elegance')
        #style.theme_use('equilux')
        #style.theme_use('itft1')
        #style.theme_use('kroc')
        #style.theme_use('plastik')
        #style.theme_use('radiance')
        #style.theme_use('scidblue')
        #style.theme_use('smog')
        #style.theme_use('ubuntu')
        #style.theme_use('winxpblue')

        # Establece el tamaño de la ventana y su título
        self.panel.geometry('1230x610')
        self.panel.title(f'Panel de administración - {self.ver_tabla}')

        # Configura la columna principal del panel para que use todo el espacio disponible
        self.panel.columnconfigure(0, weight=1)

        # Crea las variables para los campos de consulta
        self.variable_corte_numero = StringVar()
        self.variable_folio = StringVar()
        self.variable_fecha_inicio_entrada = StringVar()
        self.variable_fecha_fin_entrada = StringVar()
        self.variable_fecha_inicio_salida = StringVar()
        self.variable_fecha_fin_salida = StringVar()

        #instancia de la clase de herramientas
        tools_instance = tools()
        icono_calendario = tools_instance.read_path_config_file('images', 'icono_calendario')

        # Crea las variables para el icono de calendario
        self.icono_calendario = PhotoImage(file=icono_calendario).subsample(25)

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

        # Inicia el loop principal de la ventana
        self.panel.mainloop()


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
        seccion_tabla.grid(row=0, column=0, sticky='nsew')


        # Obtiene los nombres de las columnas de la tabla que se va a mostrar
        columnas = self.query.obtener_campos_tabla(self.ver_tabla)

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
        self.tabla.column('#2', width=120, stretch=False)
        self.tabla.column('#3', width=120, stretch=False)
        self.tabla.column('#4', width=100, stretch=False)
        self.tabla.column('#5', width=60, stretch=False)
        self.tabla.column('#6', width=60, stretch=False)
        self.tabla.column('#7', width=60, stretch=False)
        self.tabla.column('#8', width=60, stretch=False)
        self.tabla.column('#9', width=100, stretch=False)
        self.tabla.column('#10', width=90, stretch=False)
        self.tabla.column('#11', width=75, stretch=False)

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

    def view_campos_consulta(self):
        '''Crea y empaqueta los campos de consulta en la ventana.'''

        # Crear una seccion para todos los campos de texto
        seccion_campos_consulta = ttk.LabelFrame(self.panel, text='Consulta de datos', padding=10)
        seccion_campos_consulta.grid(row=0, column=2, sticky='n')


        seccion_botones_ayuda = ttk.LabelFrame(seccion_campos_consulta, text='Botones', padding=10)
        seccion_botones_ayuda.grid(row=1, column=0, sticky='')



        #######################################################################---
        # Crear un boton para vaciar todos los campos
        boton_vaciar_campos = ttk.Button(seccion_botones_ayuda, text='Vaciar campos', command=self.vaciar_campos)
        boton_vaciar_campos.grid(row=0, column=0, sticky='')

        # Crea un botón para ver todos los registros
        boton_ver_todo = ttk.Button(seccion_botones_ayuda, text='Ver todo', command=self.ver_tabla_completa)
        boton_ver_todo.grid(row=1, column=0, sticky='')
        #######################################################################---






        # Crear un LabelFrame para la consulta de corte y folio
        seccion_consulta = ttk.LabelFrame(seccion_campos_consulta, text='Consulta')
        seccion_consulta.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de corte
        etiqueta_corte = ttk.Label(seccion_consulta, text='Corte: ')
        etiqueta_corte.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto para la consulta de corte
        self.campo_texto_corte = tk.Entry(seccion_consulta, textvariable=self.variable_corte_numero)
        self.campo_texto_corte.grid(row=0, column=1, padx=5, pady=5)
        #######################################################################---

        #######################################################################---
        # Crear la leyenda para el campo de texto de la consulta de folio
        etiqueta_folio = ttk.Label(seccion_consulta, text='Folio: ')
        etiqueta_folio.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        # Crear los campos de texto para la consulta de folio
        self.campo_texto_folio = tk.Entry(seccion_consulta, textvariable=self.variable_folio)
        self.campo_texto_folio.grid(row=3, column=1, padx=5, pady=5)
        #######################################################################---





        #######################################################################---
        # Crear un LabelFrame para las entradas
        seccion_entrada = ttk.LabelFrame(seccion_campos_consulta, text='Entradas')
        seccion_entrada.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')



        # Crear el boton para el calendario entrada inicio
        boton_calendario_inicio_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, width=5, command= self.actualizar_fecha_inicio_entrada)
        boton_calendario_inicio_entrada.grid(row=0, column=0, sticky=tk.W)

        # Crear las leyendas para los campos de texto de las entradas
        etiqueta_fecha_inicio_entrada = ttk.Label(seccion_entrada, text='Fecha inicio:', width=12, anchor=tk.W)
        etiqueta_fecha_inicio_entrada.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
       
        # Crear los campos de texto para las entradas
        self.campo_texto_entrada_fecha_inicio = ttk.Label(seccion_entrada, text='')
        self.campo_texto_entrada_fecha_fin = tk.Label(seccion_entrada, text='')



        # Crear el boton para el calendario entrada fin
        boton_calendario_fin_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, width=5, command=self.actualizar_fecha_fin_entrada)
        boton_calendario_fin_entrada.grid(row=1, column=0, sticky=tk.W)

        etiqueta_fecha_fin_entrada = ttk.Label(seccion_entrada, text='Fecha fin:')
        etiqueta_fecha_fin_entrada.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las entradas
        self.campo_texto_entrada_fecha_inicio.grid(row=0, column=2, padx=5, pady=5,sticky='nsew')
        self.campo_texto_entrada_fecha_fin.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        #######################################################################---





        #######################################################################---
        # Crear un LabelFrame para las salidas
        seccion_salida = ttk.LabelFrame(seccion_campos_consulta, text='Salidas')
        seccion_salida.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')



        # Crear el boton para el calendario salida inicio
        boton_calendario_inicio_salida = ttk.Button(seccion_salida, image=self.icono_calendario, width=5, command=self.actualizar_fecha_inicio_salida)
        boton_calendario_inicio_salida.grid(row=0, column=0, sticky=tk.W)


        # Crear los campos de texto para las salidas
        self.campo_texto_salida_fecha_inicio = tk.Label(seccion_salida, text='')
        self.campo_texto_salida_fecha_fin = tk.Label(seccion_salida, text='')

        # Crear las leyendas para los campos de texto de las salidas
        etiqueta_fecha_inicio_salida = ttk.Label(seccion_salida, text='Fecha inicio:')
        etiqueta_fecha_inicio_salida.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)




        # Crear el boton para el calendario salida fin
        boton_calendario_fin_salida = ttk.Button(seccion_salida, image=self.icono_calendario, width=5, command=self.actualizar_fecha_fin_salida)
        boton_calendario_fin_salida.grid(row=1, column=0, sticky=tk.W)

        etiqueta_fecha_fin_salida = ttk.Label(seccion_salida, text='Fecha fin:')
        etiqueta_fecha_fin_salida.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las salidas
        self.campo_texto_salida_fecha_inicio.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        self.campo_texto_salida_fecha_fin.grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
        #######################################################################---




        #######################################################################---
        # Crea un LabelFrame para los botones de consulta
        seccion_botones_consulta = ttk.LabelFrame(seccion_campos_consulta, text='Consulta')
        seccion_botones_consulta.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_consulta = ttk.Button(seccion_botones_consulta, text='Consulta', command=self.hacer_consulta, width=15)
        boton_consulta.grid(row=0, column=0, pady=5)


        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_generar_reporte = ttk.Button(seccion_botones_consulta, text='Generar reporte', width=15, command = self.realizar_reporte)
        boton_generar_reporte.grid(row=2, column=0, pady=5)

        # Crea un LabelFrame para los botones de desconectar y salir
        seccion_botones_salir = ttk.LabelFrame(seccion_campos_consulta, text='Salir')
        seccion_botones_salir.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_desconectar = ttk.Button(seccion_botones_salir, text='Desconectar', width=15)
        boton_desconectar.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_salir = ttk.Button(seccion_botones_salir, text='Salir', command=self.salir, width=15)
        boton_salir.grid(row=2, column=0, pady=5)
        #######################################################################---




    def hacer_consulta(self):
        """
        Realiza una consulta SQL con los valores proporcionados por el usuario y llena la tabla con los registros obtenidos.
        """
        try:
            parametros = {}

            # Obtener los valores de los campos de consulta
            fecha_inicio_entrada = self.variable_fecha_inicio_entrada.get()
            fecha_fin_entrada = self.variable_fecha_fin_entrada.get()
            fecha_inicio_salida = self.variable_fecha_inicio_salida.get()
            fecha_fin_salida = self.variable_fecha_fin_salida.get()
            corte_numero = self.variable_corte_numero.get()
            id = self.variable_folio.get()

            # Validar y agregar los parámetros a la consulta
            if fecha_inicio_entrada != '':
                if len(fecha_inicio_entrada) < 19 or len(fecha_inicio_entrada) > 19:
                    raise TypeError('Error, el valor de los campos es superior a 19 caracteres')
                parametros['fecha_inicio_entrada'] = str(fecha_inicio_entrada)

            if fecha_fin_entrada != '':
                if len(fecha_fin_entrada) != 19:
                    raise TypeError('Error, el valor de los campos es superior a 19 caracteres')
                parametros['fecha_fin_entrada'] = str(fecha_fin_entrada)

            if fecha_inicio_salida != '':
                if len(fecha_inicio_salida) != 19:
                    raise TypeError('Error, el valor de los campos es superior a 19 caracteres')
                parametros['fecha_inicio_salida'] = str(fecha_inicio_salida)

            if fecha_fin_salida != '':
                parametros['fecha_fin_salida'] = str(fecha_fin_salida)
                if len(fecha_fin_salida) != 19:
                    raise TypeError('Error, el valor de los campos es superior a 19 caracteres')

            if corte_numero != '':
                parametros['corte_numero'] = int(corte_numero)

            if id != '':
                parametros['id'] = int(id)

            # Validar que se hayan proporcionado parámetros para la consulta
            if parametros == {}:raise ValueError('Error: los campos están vacíos')

            # Realizar la consulta y llenar la tabla con los resultados
            self.registros = self.query.hacer_consulta_sql_entradas(parametros)
            self.llenar_tabla(self.registros)

        except ValueError:
            messagebox.showwarning('Error', 'Por favor introduzca un dato válido para realizar la consulta.')
        except TypeError:
            messagebox.showwarning('Error', 'El formato de la fecha ingresada no es correcto o la fecha ingresada no es válida')


    def salir(self):
        """
        Muestra un cuadro de diálogo para informar al usuario que se está cerrando la aplicación y destruye el panel principal.
        """
        # Muestra un cuadro de diálogo con el mensaje "Hasta pronto"
        messagebox.showinfo('Salida', 'Hasta pronto.')
        # Destruye el panel principal
        self.panel.destroy()

    
    def ver_tabla_completa(self):
        '''Método para visualizar la tabla completa sin restricciones.'''
        if messagebox.askokcancel(title='Advertencia',message='Para ver todos los registros de la tabla, debe considerar que para reaizar esta consulta el tiempo de respuesta puede variar desde unos segundos hasta minutos, pasaria lo mismo si quiere realizar un reporte de esta tabla.\n\n\t\t ¿Quiere continuar?'):
        # Obtiene todos los registros
            registros = self.query.obtener_registros_completos(self.ver_tabla)
            
            # Llena la tabla con los registros
            self.llenar_tabla(registros)


    def llenar_tabla(self, registros):
        '''Llena la tabla con los registros que cumplen con los criterios de búsqueda.

        Parameters:
        registros: list
            Una lista de tuplas que representan los registros obtenidos de la base de datos.
        '''
        # Limpia la tabla antes de llenarla con nuevos registros
        self.vaciar_tabla()

        # Si no hay registros que correspondan a la consulta, muestra un mensaje informativo
        if len(registros) == 0:
            messagebox.showinfo('Info', 'No hay registros que correspondan a la consulta establecida.')

        # Itera a través de los registros y los inserta en la tabla
        for registro in registros:
            self.tabla.insert('', 'end', values=registro)


    def vaciar_tabla(self):
        """
        Elimina todas las filas de la tabla.
        """
        # Elimina todas las filas de la tabla
        self.tabla.delete(*self.tabla.get_children())


    def realizar_reporte(self):
        """
        Realiza un reporte de los registros obtenidos en una consulta y lo guarda en un archivo de Excel.

        Raises:
            TypeError: Si no se ha realizado una consulta antes de generar un reporte.
            ValueError: Si la consulta está vacía y no se puede generar un reporte.
            AttributeError: Si hay valores inválidos en los campos Entrada o Salida para realizar la consulta.
        """

        try:
            # Verificar que se haya realizado una consulta antes de generar un reporte
            if self.registros == None:raise TypeError('Error: no se ha realizado una consulta antes de generar un reporte')
            if len(self.registros) == 0:raise ValueError('Error: la consulta esta vacia y no se puede generar un reporte')

            # Obtener los valores de los campos de entrada y salida, corte_numero e id
            fecha_inicio_entrada = self.variable_fecha_inicio_entrada.get()
            fecha_fin_entrada = self.variable_fecha_fin_entrada.get()
            fecha_inicio_salida = self.variable_fecha_inicio_salida.get()
            fecha_fin_salida = self.variable_fecha_fin_salida.get()
            corte_numero = self.variable_corte_numero.get()
            id = self.variable_folio.get()

            # Obtener la ruta y el nombre del archivo donde se guardará el reporte
            ruta_archivo = filedialog.asksaveasfilename(defaultextension='.xlsx', initialfile=f'reporte_')

            # Crear un archivo de Excel y escribir los registros
            workbook = xlsxwriter.Workbook(ruta_archivo)
            worksheet = workbook.add_worksheet()

            # Obtener las columnas de la tabla
            columnas = self.query.obtener_campos_tabla(self.ver_tabla)

            # Establecer el nombre de las columnas en la primera fila
            for i in range(len(columnas)):
                worksheet.write(0, i, columnas[i])

            # Escribir los registros
            for i, registro in enumerate(self.registros):
                for j, valor in enumerate(registro):
                    # Si el campo es "Entrada" o "Salida", convertir a fecha y hora
                    if columnas[j] == 'Entrada':
                        fecha_hora = datetime.strptime(valor.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                        fecha_hora_str = datetime.strftime(fecha_hora, '%Y-%m-%d %H:%M:%S')
                        worksheet.write(i+1, j, fecha_hora_str)
                    elif columnas[j] == 'Salida':
                        fecha_hora = datetime.strptime(valor.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                        fecha_hora_str = datetime.strftime(fecha_hora, '%Y-%m-%d %H:%M:%S')
                        worksheet.write(i+1, j, fecha_hora_str)
                    else:
                        worksheet.write(i+1, j, valor)

            # Escribir la fórmula de suma
            columna_importe = columnas.index('Importe')
            ultima_fila = len(self.registros) + 1
            num_registros = len(self.registros)
            if num_registros > 0:
                suma_importe = f'=SUM({xlsxwriter.utility.xl_rowcol_to_cell(1, columna_importe)}:{xlsxwriter.utility.xl_rowcol_to_cell(num_registros, columna_importe)})'
                worksheet.write_formula(num_registros+4, columna_importe, suma_importe)

            # Cerrar el archivo de Excel
            workbook.close()
            messagebox.showinfo('Mensaje', 'El reporte fue generado con exito')
            self.vaciar_campos()

        #Manejo de errores
        except TypeError:messagebox.showerror('Error', 'Para realizar un reporte primero tiene que realizar una consulta')
        except ValueError:messagebox.showerror('Error', 'Para realizar un reporte primero tiene que realizar una consulta que contenga registros')
        except AttributeError:messagebox.showerror('Error', 'El reporte no se puede generar ya que en los campos Entrada o Salida hay valores invalidos para realizar la consulta, favor de revisar y volver a intentar')
        except exceptions.FileCreateError:messagebox.showerror('Error', 'El reporte no se puede generar, seleccione el directorio para guardar el reporte y vuelva a intentar')


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


        self.campo_texto_entrada_fecha_inicio.config(text="")
        self.campo_texto_entrada_fecha_fin.config(text="")


        self.campo_texto_salida_fecha_fin.config(text="")
        self.campo_texto_salida_fecha_inicio.config(text="")

        # Limpia las variables de control
        self.variable_corte_numero.set('')
        self.variable_folio.set('')
        self.variable_fecha_inicio_entrada.set('')
        self.variable_fecha_fin_entrada.set('')
        self.variable_fecha_inicio_salida.set('')
        self.variable_fecha_fin_salida.set('')


    def actualizar_fecha_inicio_entrada(self):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.
        """

        def obtener_fecha():
            """
            Función interna que se encarga de mostrar el calendario y obtener la fecha seleccionada por el usuario.
            """
            self.calendario_fecha_inicio_entrada = Fecha_Hora()
            self.calendario_fecha_inicio_entrada.mostrar_calendario()

            self.fecha_hora_inicio_entrada = self.calendario_fecha_inicio_entrada.selected_datetime

            self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

            # Elimina cualquier texto existente en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text="")

            # Inserta el nuevo valor en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)

        # Se inicia un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario
        t = threading.Thread(name='Calendario',target=obtener_fecha)
        t.start()


    def actualizar_fecha_fin_entrada(self):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.
        """

        def obtener_fecha():
            """
            Función interna que se encarga de mostrar el calendario y obtener la fecha seleccionada por el usuario.
            """
            self.calendario_fecha_inicio_entrada = Fecha_Hora()
            self.calendario_fecha_inicio_entrada.mostrar_calendario()

            self.fecha_hora_inicio_entrada = self.calendario_fecha_inicio_entrada.selected_datetime

            self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

            # Elimina cualquier texto existente en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text="")

            # Inserta el nuevo valor en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)

        # Se inicia un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario
        t = threading.Thread(target=obtener_fecha)
        t.start()


    def actualizar_fecha_inicio_salida(self):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.
        """

        def obtener_fecha():
            """
            Función interna que se encarga de mostrar el calendario y obtener la fecha seleccionada por el usuario.
            """
            self.calendario_fecha_inicio_entrada = Fecha_Hora()
            self.calendario_fecha_inicio_entrada.mostrar_calendario()

            self.fecha_hora_inicio_entrada = self.calendario_fecha_inicio_entrada.selected_datetime

            self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

            # Elimina cualquier texto existente en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text="")

            # Inserta el nuevo valor en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)

        # Se inicia un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario
        t = threading.Thread(target=obtener_fecha)
        t.start()


    def actualizar_fecha_fin_salida(self):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.
        """

        def obtener_fecha():
            """
            Función interna que se encarga de mostrar el calendario y obtener la fecha seleccionada por el usuario.
            """
            self.calendario_fecha_inicio_entrada = Fecha_Hora()
            self.calendario_fecha_inicio_entrada.mostrar_calendario()

            self.fecha_hora_inicio_entrada = self.calendario_fecha_inicio_entrada.selected_datetime

            self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

            # Elimina cualquier texto existente en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text="")

            # Inserta el nuevo valor en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)

        # Se inicia un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario
        t = threading.Thread(target=obtener_fecha)
        t.start()

