from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import TclError
import sys
import os
from Models.queries import Queries


class Aplicacion:
    """Clase principal que maneja la interfaz gráfica del usuario."""
    
    def __init__(self, ver_tabla):
        """
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.

        Args:
        ver_tabla (str): nombre de la tabla que se va a visualizar en la interfaz.
        """

        self.ver_tabla = ver_tabla
        self.panel = tk.Tk()
        self.panel.geometry("1200x400")
        self.panel.title("Panel de administración")
        self.panel.columnconfigure(0, weight=1)  # Configurar la columna principal del panel


        self.variable_corte_numero = IntVar(value = 0)
        self.variable_fecha_inicio = BooleanVar(value = 0) 
        self.variable_fecha_fin = BooleanVar(value = 0)        
        self.variable_folio = IntVar(value = 0)

        self.query = Queries()
        self.message = None
        self.tabla = None


        self.view_tabla()

        self.campos_consulta()

        self.panel.mainloop()


    def view_tabla(self):
        """
        Crea la tabla en la interfaz y la llena con los datos de la base de datos.
        """

        seccion_tabla = ttk.LabelFrame(self.panel, text=f"Tabla - {self.ver_tabla}")
        seccion_tabla.columnconfigure(0, weight=1, uniform="tabla")
        seccion_tabla.grid_propagate(True)
        seccion_tabla.grid(row=0, column=0, sticky="nsew")

        
        campos = self.query.obtener_campos_tabla(self.ver_tabla)

        # Crea un Treeview con una columna por cada campo de la tabla
        self.tabla = ttk.Treeview(seccion_tabla, columns=(campos))
        self.tabla.config(height=15)

        # Define los encabezados de columna
        i = 1
        for headd in (campos):
            self.tabla.heading(f"#{i}", text=headd)
            self.tabla.column(f"#{i}", width=100)
            i = i + 1
        self.tabla.column("#0", width=5, stretch=False)
        self.tabla.column("#1", width=50, stretch=False)
        self.tabla.column("#2", width=120, stretch=False)
        self.tabla.column("#3", width=120, stretch=False)

        # Inserta datos
        self.ver_tabla_completa()

        # Crea un Scrollbar vertical y lo asocia con el Treeview
        scrollbar_Y = ttk.Scrollbar(seccion_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar_Y.set)
        scrollbar_Y.grid(row=0, column=1, sticky="NS")

        # Crea un Scrollbar horizontal y lo asocia con el Treeview
        scrollbar_X = ttk.Scrollbar(seccion_tabla, orient="horizontal", command=self.tabla.xview)
        self.tabla.configure(xscroll=scrollbar_X.set)
        scrollbar_X.grid(row=1, column=0, sticky="EW")

        # Empaqueta el Treeview en la ventana
        self.tabla.grid(row=0, column=0, sticky="NESW")


    def campos_consulta(self):
        """Crea y empaqueta los campos de consulta en la ventana."""

        # Crear un seccion_campos_consulta para los campos de texto
        seccion_campos_consulta = ttk.LabelFrame(self.panel, text="Consulta de datos", padding=10)
        seccion_campos_consulta.grid(row=0, column=1, sticky='n')

        # Crear los campos de texto
        self.campo_texto_corte = tk.Entry(seccion_campos_consulta, textvariable = self.variable_corte_numero)
        self.campo_texto_fecha_inicio = tk.Entry(seccion_campos_consulta, textvariable = self.variable_fecha_inicio)
        self.campo_texto_fecha_fin = tk.Entry(seccion_campos_consulta, textvariable = self.variable_fecha_fin)
        self.campo_texto_folio = tk.Entry(seccion_campos_consulta, textvariable = self.variable_folio)

        # Empaqueta los campos de texto en el seccion_campos_consulta
        self.campo_texto_corte.grid(row=0, column=1, padx=5, pady=5)
        self.campo_texto_fecha_inicio.grid(row=1, column=1, padx=5, pady=5)
        self.campo_texto_fecha_fin.grid(row=2, column=1, padx=5, pady=5)
        self.campo_texto_folio.grid(row=3, column=1, padx=5, pady=5)

        # Crear las leyendas para los campos de texto
        leyenda_corte = ttk.Label(seccion_campos_consulta, text="Corte: ")
        leyenda_fecha_inicio = ttk.Label(seccion_campos_consulta, text="Fecha inicio: ")
        leyenda_fecha_fin = ttk.Label(seccion_campos_consulta, text="Fecha fin: ")
        leyenda_folio = ttk.Label(seccion_campos_consulta, text="Folio: ")

        # Empaqueta las leyendas y los campos de texto en el seccion_campos_consulta
        leyenda_corte.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        leyenda_fecha_inicio.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        leyenda_fecha_fin.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        leyenda_folio.grid(row=3, column=0, padx=5, pady=5, sticky="W")

        # Crea un botón y lo empaqueta en el seccion_campos_consulta
        boton_consulta = tk.Button(seccion_campos_consulta, text="Consulta", command=self.hacer_consulta)
        boton_consulta.grid(row=4, column=1)

        # Crea un botón y lo empaqueta en el seccion_campos_consulta
        boton_ver_todo = tk.Button(seccion_campos_consulta, text="Ver todo", command=self.ver_tabla_completa)
        boton_ver_todo.grid(row=5, column=1)

        boton_generar_reporte = tk.Button(seccion_campos_consulta, text="Generar reporte")
        boton_generar_reporte.grid(row=6, column=1)

        boton_desconectar = tk.Button(seccion_campos_consulta, text="Desconectar")
        boton_desconectar.grid(row=8, column=1)

        boton_salir = tk.Button(seccion_campos_consulta, text="Salir", command = self.salir)
        boton_salir.grid(row=10, column=1)
    
    def hacer_consulta(self):
        try:
            registros = self.query.obtener_registros_corte_numero(self.ver_tabla, int(self.variable_corte_numero.get()))

            self.llenar_tabla(registros)

        except TclError:
            messagebox.showerror("Error", "Por favor introduzca un dato valido para realizar la consulta.")

    def salir(self):
        messagebox.showinfo("Salida", "Hasta pronto.")
        self.panel.destroy()
    
    def ver_tabla_completa(self):
        # Inserta datos
        registros = self.query.obtener_registros(self.ver_tabla)
        self.llenar_tabla(registros)


    def llenar_tabla(self, registros):
        """Método auxiliar para llenar la tabla con los registros que cumplen con los criterios de búsqueda."""
        self.vaciar_tabla()
        for registro in registros:
            self.tabla.insert("", "end", values=registro)


    def vaciar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())


