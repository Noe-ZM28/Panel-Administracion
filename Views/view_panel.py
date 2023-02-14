import tkinter as tk

from datetime import datetime, date, time, timedelta
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from tkinter import font
from tkinter import *
from tkinter import simpledialog
class FormularioOperacion:
    def __init__(self):
        #creamos un objeto que esta en el archivo operacion dentro la clase Operacion
        self.ventana1=tk.Tk()
        self.ventana1.title("Generar reportes")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.cuaderno1.config(cursor="")         # Tipo de cursor
        self.ExpedirRfid()


        self.cuaderno1.grid(column=0, row=0, padx=5, pady=5)
        self.ventana1.mainloop()
        ####################Inicia Pagina1###################


    def ExpedirRfid(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Expedir Boleto")


        #enmarca los controles LabelFrame
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Dar Entrada")
        self.labelframe1.grid(column=1, row=0, padx=0, pady=0)
        self.MaxId=tk.StringVar()
        self.entryMaxId=ttk.Entry(self.labelframe1, width=10, textvariable=self.MaxId, state="readonly")
        self.entryMaxId.grid(column=1, row=0, padx=4, pady=4)
        self.lbltitulo=ttk.Label(self.labelframe1, text="FOLIO")
        self.lbltitulo.grid(column=0, row=0, padx=0, pady=0)


        #####tomar placas del auto
        self.Placa=tk.StringVar()
        self.entryPlaca=tk.Entry(self.labelframe1, width=10, textvariable=self.Placa)
        self.entryPlaca.grid(column=1, row=1, padx=4, pady=4)
        self.lblPlaca=ttk.Label(self.labelframe1, text="COLOCAR PLACAS")
        self.lblPlaca.grid(column=0, row=1, padx=0, pady=0)






        #Boton - Salir del programa
        self.boton2=tk.Button(self.pagina1, text="Salir del programa", command=quit, width=15, height=1, anchor="center")
        self.boton2.grid(column=0, row=0, padx=4, pady=4)

aplicacion1=FormularioOperacion()
