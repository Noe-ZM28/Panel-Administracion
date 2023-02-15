import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

import sys
import os

# Ahora deberías poder importar la clase DatabaseConfig
from Models.querys import Querys

class Aplicacion:
    def __init__(self, ver_tabla):
        self.ver_tabla = ver_tabla
        self.panel=tk.Tk()
        self.panel.geometry("1200x400")
        self.panel.title("Panel de administración")

        self.tabla()
        self.panel.columnconfigure(0, weight=1)  # Configurar la columna principal del panel

        self.campos_consulta()


        self.panel.mainloop()


    def tabla(self):
        seccion_tabla = ttk.LabelFrame(self.panel, text=f"Tabla - {self.ver_tabla}")
        seccion_tabla.columnconfigure(0, weight=1, uniform="tabla")
        seccion_tabla.grid_propagate(True)

        seccion_tabla.grid(row=0, column=0, sticky="nsew")
        


        query = Querys()
        campos = query.obtener_campos_tabla(self.ver_tabla)

        # Crea un Treeview con una columna por cada campo de la tabla
        tabla = ttk.Treeview(seccion_tabla, columns=(campos))
        tabla.config(height=15)


        # Define los encabezados de columna
        i = 1
        for headd in (campos):
            tabla.heading(f"#{i}", text=headd)
            tabla.column(f"#{i}", width=100)
            i = i + 1
        tabla.column("#0", width=5, stretch=False)
        tabla.column("#1", width=50, stretch=False)

        # Inserta datos
        registros = query.obtener_registros(self.ver_tabla)
        for registro in registros:
            tabla.insert("", "end", values=registro)

        # Crea un Scrollbar vertical y lo asocia con el Treeview
        scrollbar_Y = ttk.Scrollbar(seccion_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscroll=scrollbar_Y.set)
        scrollbar_Y.grid(row=0, column=1, sticky="NS")

        # Crea un Scrollbar horizontal y lo asocia con el Treeview
        scrollbar_X = ttk.Scrollbar(seccion_tabla, orient="horizontal", command=tabla.xview)
        tabla.configure(xscroll=scrollbar_X.set)
        scrollbar_X.grid(row=1, column=0, sticky="EW")




        # Empaqueta el Treeview en la ventana
        tabla.grid(row=0, column=0, sticky="NESW")



    def llenar_tabla(self):
        pass
        


    def campos_consulta(self):
        # Crear un seccion_campos_consulta para los campos de texto
        seccion_campos_consulta = ttk.LabelFrame(self.panel, text="Consulta de datos", padding=10)
        seccion_campos_consulta.grid(row=0, column=1, sticky='n')
        
        # Crear los campos de texto
        self.campo_texto_corte = tk.Entry(seccion_campos_consulta)
        self.campo_texto_fecha_inicio = tk.Entry(seccion_campos_consulta)
        self.campo_texto_fecha_fin = tk.Entry(seccion_campos_consulta)
        self.campo_texto_folio = tk.Entry(seccion_campos_consulta)
        
        # Empaqueta los campos de texto en el seccion_campos_consulta
        self.campo_texto_corte.grid(row=0, column=0)
        self.campo_texto_fecha_inicio.grid(row=1, column=0)
        self.campo_texto_fecha_fin.grid(row=2, column=0)
        self.campo_texto_folio.grid(row=3, column=0)
        

        # Crear las leyendas para los campos de texto
        leyenda_corte = ttk.Label(seccion_campos_consulta, text="Corte:")
        leyenda_fecha_inicio = ttk.Label(seccion_campos_consulta, text="Fecha inicio:")
        leyenda_fecha_fin = ttk.Label(seccion_campos_consulta, text="Fecha fin:")
        leyenda_folio = ttk.Label(seccion_campos_consulta, text="Folio:")

        # Empaqueta las leyendas y los campos de texto en el seccion_campos_consulta
        leyenda_corte.grid(row=0, column=0, padx=5, pady=5, sticky="W")
        self.campo_texto_corte.grid(row=0, column=1, padx=5, pady=5)
        leyenda_fecha_inicio.grid(row=1, column=0, padx=5, pady=5, sticky="W")
        self.campo_texto_fecha_inicio.grid(row=1, column=1, padx=5, pady=5)
        leyenda_fecha_fin.grid(row=2, column=0, padx=5, pady=5, sticky="W")
        self.campo_texto_fecha_fin.grid(row=2, column=1, padx=5, pady=5)
        leyenda_folio.grid(row=3, column=0, padx=5, pady=5, sticky="W")
        self.campo_texto_folio.grid(row=3, column=1, padx=5, pady=5)




        # Crea un botón y lo empaqueta en el seccion_campos_consulta
        boton_consulta = tk.Button(seccion_campos_consulta, text="Consulta")
        boton_consulta.grid(row=4, column=0)

        boton_generar_reporte = tk.Button(seccion_campos_consulta, text="Generar reporte")
        boton_generar_reporte.grid(row=5, column=0)

    def mostrar_mensaje(self):
        """Muestra un mensaje en una ventana emergente."""
        mensaje = tk.messagebox.showinfo("Mensaje", "Boton presionado")

