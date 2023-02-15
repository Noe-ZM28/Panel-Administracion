import tkinter as tk

from tkinter import ttk
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        self.panel=tk.Tk()
        self.panel.geometry("800x300")
        self.panel.title("Panel de administración")

        self.tabla()
        self.panel.columnconfigure(0, weight=1)  # Configurar la columna principal del panel

        self.campos_consulta()


        self.panel.mainloop()


    def tabla(self):
        seccion_tabla = ttk.LabelFrame(self.panel, text="Tabla")
        seccion_tabla.grid(row=0, column=0)

        # Crea un Treeview con 3 columnas
        tabla = ttk.Treeview(seccion_tabla, columns=("Nombre", "Apellido", "Edad"))

        # Define los encabezados de columna
        tabla.heading("#0", text="ID")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Apellido", text="Apellido")
        tabla.heading("Edad", text="Edad")

        # Inserta datos de ejemplo
        tabla.insert("", "end", text="1", values=("Juan", "Pérez", 25))
        tabla.insert("", "end", text="2", values=("María", "González", 30))
        tabla.insert("", "end", text="3", values=("Pedro", "García", 35))
        tabla.insert("", "end", text="1", values=("Juan", "Pérez", 25))

        # Ajusta el ancho de cada columna
        tabla.column("#0", width=50, stretch = True)
        tabla.column("Nombre", width=100)
        tabla.column("Apellido", width=100)
        tabla.column("Edad", width=50)

        # Crea un Scrollbar vertical y lo asocia con el Treeview
        scrollbar = ttk.Scrollbar(seccion_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Empaqueta el Treeview en la ventana
        tabla.pack(anchor='n', fill="both", expand=True)

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

if __name__ == "__main__":
    app = Aplicacion()
