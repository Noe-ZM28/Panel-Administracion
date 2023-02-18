from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import TclError
import sys
import os
from Models.queries import Queries


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
        self.panel.geometry('1170x550')

        self.panel.title(f'Panel de administración - {self.ver_tabla}')
        self.panel.columnconfigure(0, weight=1)  # Configurar la columna principal del panel


        self.variable_corte_numero = StringVar()
        self.variable_folio = StringVar()


        self.variable_fecha_inicio_entrada = StringVar()
        self.variable_fecha_fin_entrada = StringVar()

        self.variable_fecha_inicio_salida = StringVar()
        self.variable_fecha_fin_salida = StringVar()      


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
        # Crear un seccion_campos_consulta para los campos de texto
        seccion_campos_consulta = ttk.LabelFrame(self.panel, text='Consulta de datos', padding=10)
        seccion_campos_consulta.grid(row=0, column=2, sticky='n')


        # Crear un LabelFrame para la consulta de corte
        seccion_consulta = ttk.LabelFrame(seccion_campos_consulta, text='Consulta')
        seccion_consulta.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        # Crear los campos de texto para la consulta de corte
        self.campo_texto_corte = tk.Entry(seccion_consulta, textvariable=self.variable_corte_numero)

        # Crear la leyenda para el campo de texto de la consulta de corte
        leyenda_corte = ttk.Label(seccion_consulta, text='Corte: ')
        leyenda_corte.grid(row=0, column=0, padx=5, pady=5, sticky='W')

        # Empaquetar el campo de texto y la leyenda en el LabelFrame de la consulta de corte
        self.campo_texto_corte.grid(row=0, column=1, padx=5, pady=5)

        self.campo_texto_folio = tk.Entry(seccion_consulta, textvariable = self.variable_folio)
        self.campo_texto_folio.grid(row=3, column=1, padx=5, pady=5)
        leyenda_folio = ttk.Label(seccion_consulta, text='Folio: ')
        leyenda_folio.grid(row=3, column=0, padx=5, pady=5, sticky='W')


        # Crear un LabelFrame para las entradas
        seccion_entrada = ttk.LabelFrame(seccion_campos_consulta, text='Entradas')
        seccion_entrada.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        # Crear los campos de texto para las entradas
        self.campo_texto_entrada_fecha_inicio = tk.Entry(seccion_entrada, textvariable=self.variable_fecha_inicio_entrada)
        self.campo_texto_entrada_fecha_fin = tk.Entry(seccion_entrada, textvariable=self.variable_fecha_fin_entrada)

        # Crear las leyendas para los campos de texto de las entradas
        leyenda_fecha_inicio = ttk.Label(seccion_entrada, text='Fecha inicio:')
        leyenda_fecha_inicio.grid(row=0, column=0, padx=5, pady=5, sticky='W')

        leyenda_fecha_fin = ttk.Label(seccion_entrada, text='Fecha fin:')
        leyenda_fecha_fin.grid(row=1, column=0, padx=5, pady=5, sticky='W')

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las entradas
        self.campo_texto_entrada_fecha_inicio.grid(row=0, column=1, padx=5, pady=5)
        self.campo_texto_entrada_fecha_fin.grid(row=1, column=1, padx=5, pady=5)

        # Crear un LabelFrame para las salidas
        seccion_salida = ttk.LabelFrame(seccion_campos_consulta, text='Salidas')
        seccion_salida.grid(row=3, column=0, padx=5, pady=5, sticky='w')


        # Crear los campos de texto para las salidas
        self.campo_texto_salida_fecha_inicio = tk.Entry(seccion_salida, textvariable=self.variable_fecha_inicio_salida)
        self.campo_texto_salida_fecha_fin = tk.Entry(seccion_salida, textvariable=self.variable_fecha_fin_salida)

        # Crear las leyendas para los campos de texto de las salidas
        leyenda_fecha_inicio = ttk.Label(seccion_salida, text='Fecha inicio:')
        leyenda_fecha_inicio.grid(row=0, column=0, padx=5, pady=5, sticky='W')

        leyenda_fecha_fin = ttk.Label(seccion_salida, text='Fecha fin:')
        leyenda_fecha_fin.grid(row=1, column=0, padx=5, pady=5, sticky='W')

        # Empaqueta los campos de texto y las leyendas en el LabelFrame de las salidas
        self.campo_texto_salida_fecha_inicio.grid(row=0, column=1, padx=5, pady=5)
        self.campo_texto_salida_fecha_fin.grid(row=1, column=1, padx=5, pady=5)



        # Crea un LabelFrame para los botones de consulta
        seccion_botones_consulta = ttk.LabelFrame(seccion_campos_consulta, text='Consulta')
        seccion_botones_consulta.grid(row=4, column=0, padx=5, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_consulta = tk.Button(seccion_botones_consulta, text='Consulta', command=self.hacer_consulta, width=15)
        boton_consulta.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_ver_todo = tk.Button(seccion_botones_consulta, text='Ver todo', command=self.ver_tabla_completa, width=15)
        boton_ver_todo.grid(row=1, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_consulta
        boton_generar_reporte = tk.Button(seccion_botones_consulta, text='Generar reporte', width=15)
        boton_generar_reporte.grid(row=2, column=0, pady=5)

        # Crea un LabelFrame para los botones de desconectar y salir
        seccion_botones_salir = ttk.LabelFrame(seccion_campos_consulta, text='Salir')
        seccion_botones_salir.grid(row=6, column=0, padx=10, pady=10)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_desconectar = tk.Button(seccion_botones_salir, text='Desconectar', width=15)
        boton_desconectar.grid(row=0, column=0, pady=5)

        # Crea un botón y lo empaqueta en la seccion_botones_salir
        boton_salir = tk.Button(seccion_botones_salir, text='Salir', command=self.salir, width=15)
        boton_salir.grid(row=2, column=0, pady=5)

    def hacer_consulta(self):
        try:
            #registros = self.query.obtener_registros_corte_numero(self.ver_tabla, int(self.variable_corte_numero.get()))
                  
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

            print("\n")
            for key in parametros:
                print (f'[{key}]:{parametros[key]}') # for the values
            print('---------------------------------')

            registros = self.query.hacer_consulta_sql_entradas(parametros)








            self.llenar_tabla(registros)
        # except TclError:
        #     messagebox.showerror('Error', 'Por favor introduzca un dato valido para realizar la consulta.')
        except ValueError:
            messagebox.showerror('Error', 'Por favor introduzca un dato valido para realizar la consulta.')



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


