from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import TclError
from Models.queries import Queries
from Views.views_tools import Fecha_Hora

import threading




class Panel_Entradas:
    '''Clase principal que maneja la interfaz gráfica del usuario.'''
    
    def __init__(self):
        '''
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.

        Args:
        ver_tabla (str): nombre de la tabla que se va a visualizar en la interfaz.
        '''
        self.ver_tabla = 'Entradas'

        self.panel = tk.Tk()
        # Permitir que la ventana no sea redimensionable
        #self.panel.resizable(width=False, height=False)
        self.panel.geometry('1170x600')
        self.panel.title(f'Panel de administración - {self.ver_tabla}')
        self.panel.columnconfigure(0, weight=1)  # Configurar la columna principal del panel


        self.variable_corte_numero = StringVar()
        self.variable_folio = StringVar()

        self.variable_fecha_inicio_entrada = StringVar()
        self.variable_fecha_fin_entrada = StringVar()

        self.variable_fecha_inicio_salida = StringVar()
        self.variable_fecha_fin_salida = StringVar()


        self.icono_calendario = PhotoImage(file='Public\Imagenes\icono_calendario.png').subsample(25)


        self.calendario_fecha_inicio_entrada = None
        self.fecha_hora_inicio_entrada = None

        self.calendario_fecha_fin_entrada = None
        self.fecha_hora_fin_entrada = None

        self.calendario_fecha_inicio_salida = None
        self.fecha_hora_inicio_salida = None

        self.calendario_fecha_fin_salida = None
        self.fecha_hora_fin_salida = None


        self.query = Queries()
        self.message = None
        self.tabla = None


        self.view_tabla()
        self.view_campos_consulta()



        self.panel.mainloop()


    def view_tabla(self):
        '''
        Crea la tabla en la interfaz y la llena con los datos de la base de datos.
        '''

        seccion_tabla = ttk.LabelFrame(self.panel, text=f'Tabla - {self.ver_tabla}')
        seccion_tabla.columnconfigure(0, weight=1, uniform='tabla')
        seccion_tabla.rowconfigure(0, weight=1)
        seccion_tabla.grid_propagate(True)
        seccion_tabla.grid(row=0, column=0, sticky='nsew')

        
        campos = self.query.obtener_campos_tabla(self.ver_tabla)

        # Crea un Treeview con una columna por cada campo de la tabla
        style = ttk.Style()

        #style.theme_use('xpnative')
        self.tabla = ttk.Treeview(seccion_tabla, columns=(campos))
        self.tabla.config(height=15)

        # Define los encabezados de columna
        i = 1
        for headd in (campos):
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
        self.ver_tabla_completa()

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
        boton_ver_todo = tk.Button(seccion_botones_ayuda, text='Ver todo', command=self.ver_tabla_completa)
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
        boton_calendario_inicio_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, width=5, command= self.actualizar_fecha_inicio)
        boton_calendario_inicio_entrada.grid(row=0, column=0, sticky=tk.W)

        # Crear las leyendas para los campos de texto de las entradas
        etiqueta_fecha_inicio_entrada = ttk.Label(seccion_entrada, text='Fecha inicio:', width=12, anchor=tk.W)
        etiqueta_fecha_inicio_entrada.config(background="lightblue")
        etiqueta_fecha_inicio_entrada.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
       
        # Crear los campos de texto para las entradas
        self.campo_texto_entrada_fecha_inicio = ttk.Label(seccion_entrada, text='')
        self.campo_texto_entrada_fecha_fin = tk.Entry(seccion_entrada, textvariable=self.variable_fecha_fin_entrada)



        # Crear el boton para el calendario entrada fin
        boton_calendario_fin_entrada = ttk.Button(seccion_entrada, image=self.icono_calendario, width=5, command=self.abrir_calendario_fin_entrada)
        boton_calendario_fin_entrada.grid(row=1, column=0, sticky=tk.W)

        etiqueta_fecha_fin_entrada = ttk.Label(seccion_entrada, text='Fecha fin:')
        etiqueta_fecha_fin_entrada.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las entradas
        self.campo_texto_entrada_fecha_inicio.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        self.campo_texto_entrada_fecha_fin.grid(row=1, column=2, padx=5, pady=5)
        #######################################################################---





        #######################################################################---
        # Crear un LabelFrame para las salidas
        seccion_salida = ttk.LabelFrame(seccion_campos_consulta, text='Salidas')
        seccion_salida.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')



        # Crear el boton para el calendario salida inicio
        boton_calendario_inicio_salida = ttk.Button(seccion_salida, image=self.icono_calendario, width=5, command=self.abrir_calendario_inicio_salida)
        boton_calendario_inicio_salida.grid(row=0, column=0, sticky=tk.W)


        # Crear los campos de texto para las salidas
        self.campo_texto_salida_fecha_inicio = tk.Entry(seccion_salida, textvariable=self.variable_fecha_inicio_salida)
        self.campo_texto_salida_fecha_fin = tk.Entry(seccion_salida, textvariable=self.variable_fecha_fin_salida)

        # Crear las leyendas para los campos de texto de las salidas
        etiqueta_fecha_inicio_salida = ttk.Label(seccion_salida, text='Fecha inicio:')
        etiqueta_fecha_inicio_salida.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)




        # Crear el boton para el calendario salida fin
        boton_calendario_fin_salida = ttk.Button(seccion_salida, image=self.icono_calendario, width=5, command=self.abrir_calendario_fin_salida)
        boton_calendario_fin_salida.grid(row=1, column=0, sticky=tk.W)

        etiqueta_fecha_fin_salida = ttk.Label(seccion_salida, text='Fecha fin:')
        etiqueta_fecha_fin_salida.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las salidas
        self.campo_texto_salida_fecha_inicio.grid(row=0, column=2, padx=5, pady=5)
        self.campo_texto_salida_fecha_fin.grid(row=1, column=2, padx=5, pady=5)
        #######################################################################---




        #######################################################################---
        # Crea un LabelFrame para los botones de consulta
        seccion_botones_consulta = ttk.LabelFrame(seccion_campos_consulta, text='Consulta')
        seccion_botones_consulta.grid(row=6, column=0, padx=5, pady=5, sticky='nsew')

        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_consulta = tk.Button(seccion_botones_consulta, text='Consulta', command=self.hacer_consulta, width=15)
        boton_consulta.grid(row=0, column=0, pady=5)


        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_generar_reporte = tk.Button(seccion_botones_consulta, text='Generar reporte', width=15)
        boton_generar_reporte.grid(row=2, column=0, pady=5)

        # Crea un LabelFrame para los botones de desconectar y salir
        seccion_botones_salir = ttk.LabelFrame(seccion_campos_consulta, text='Salir')
        seccion_botones_salir.grid(row=7, column=0, padx=10, pady=10, sticky='nsew')

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_desconectar = tk.Button(seccion_botones_salir, text='Desconectar', width=15)
        boton_desconectar.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_salir = tk.Button(seccion_botones_salir, text='Salir', command=self.salir, width=15)
        boton_salir.grid(row=2, column=0, pady=5)
        #######################################################################---




    def hacer_consulta(self):
        try:                  
            parametros = {}
            # Obtener los valores de los campos de consulta
            fecha_inicio_entrada = self.variable_fecha_inicio_entrada.get()
            fecha_fin_entrada = self.variable_fecha_fin_entrada.get()
            fecha_inicio_salida = self.variable_fecha_inicio_salida.get()
            fecha_fin_salida = self.variable_fecha_fin_salida.get()
            corte_numero = self.variable_corte_numero.get()
            id = self.variable_folio.get()


            if fecha_inicio_entrada != '': parametros['fecha_inicio_entrada'] = str(fecha_inicio_entrada)
            if fecha_fin_entrada != '': parametros['fecha_fin_entrada'] = str(fecha_fin_entrada)
            if fecha_inicio_salida != '': parametros['fecha_inicio_salida'] = str(fecha_inicio_salida)
            if fecha_fin_salida != '': parametros['fecha_fin_salida'] = str(fecha_fin_salida)
            if corte_numero != '': parametros['corte_numero'] = int(corte_numero)
            if id != '': parametros['id'] = int(id)


            if parametros == {}: raise ValueError()


            registros = self.query.hacer_consulta_sql_entradas(parametros)

            self.llenar_tabla(registros)

        except ValueError:
            messagebox.showwarning('Error', 'Por favor introduzca un dato valido para realizar la consulta.')


    def salir(self):
        messagebox.showinfo('Salida', 'Hasta pronto.')
        self.panel.destroy()
    
    def ver_tabla_completa(self):
        # Inserta datos
        registros = self.query.obtener_registros(self.ver_tabla)
        self.llenar_tabla(registros)

    def llenar_tabla(self, registros):
        '''Método auxiliar para llenar la tabla con los registros que cumplen con los criterios de búsqueda.'''
        self.vaciar_tabla()
        if len(registros) == 0: messagebox.showinfo('Info', 'No hay registros que correspondan a la consulta establecida.')
        for registro in registros:
            self.tabla.insert('', 'end', values=registro)

    def vaciar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())



    def actualizar_fecha_inicio(self):
        def obtener_fecha():
            self.calendario_fecha_inicio_entrada = Fecha_Hora()
            self.calendario_fecha_inicio_entrada.mostrar_calendario()

            self.fecha_hora_inicio_entrada = self.calendario_fecha_inicio_entrada.selected_datetime

            self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

            # Elimina cualquier texto existente en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text="")

            # Inserta el nuevo valor en la caja de texto
            self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)

        
        t = threading.Thread(target=obtener_fecha)
        t.start()




    def abrir_calendario_inicio_entrada(self):

        print('se llama la función para llamar el calendario'),
        self.calendario_fecha_inicio_entrada = Fecha_Hora()
        self.calendario_fecha_inicio_entrada.mostrar()

        print('se asigna variable')
        self.fecha_hora_inicio_entrada == self.calendario_fecha_inicio.get_selected_datetime()
        print('valor asignado: ' + self.fecha_hora_inicio_entrada)

        print('se asigna variable', +self.variable_fecha_inicio_entrada)
        self.variable_fecha_inicio_entrada.set(self.fecha_hora_inicio_entrada)

        # Elimina cualquier texto existente en la caja de texto
        self.campo_texto_entrada_fecha_inicio.config(text="")

        # Inserta el nuevo valor en la caja de texto
        self.campo_texto_entrada_fecha_inicio.config(text=self.fecha_hora_inicio_entrada)


    def abrir_calendario_fin_entrada(self):
        self.calendario_fecha_fin_entrada = Fecha_Hora()
        self.fecha_hora_fin_entrada = self.calendario_fecha_fin_entrada.selected_datetime


    def abrir_calendario_inicio_salida(self):
        self.calendario_fecha_inicio_salida = Fecha_Hora()
        self.fecha_hora_inicio_salida = self.calendario_fecha_inicio_salida.selected_datetime
        

    def abrir_calendario_fin_salida(self):
        self.calendario_fecha_fin_salida = Fecha_Hora()
        self.fecha_hora_fin_salida = self.calendario_fecha_fin_salida.selected_datetime


    def vaciar_campos(self):
        self.campo_texto_corte.delete(0, 'end')
        self.campo_texto_folio.delete(0, 'end')

        self.campo_texto_entrada_fecha_inicio.config(text="")

        self.campo_texto_entrada_fecha_fin.delete(0, 'end')
        self.campo_texto_salida_fecha_fin.delete(0, 'end')
        self.campo_texto_salida_fecha_inicio.delete(0, 'end')






        self.variable_corte_numero.set('')
        self.variable_folio.set('')


        self.variable_fecha_inicio_entrada.set('')
        self.variable_fecha_fin_entrada.set('')

        self.variable_fecha_inicio_salida.set('')
        self.variable_fecha_fin_salida.set('')