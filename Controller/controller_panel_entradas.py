from Views.views_tools import Calendar_date
from Models.queries import Queries

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


import xlsxwriter
from xlsxwriter import exceptions

from datetime import datetime

import os


class EntradasController:
    def __init__(self):
        '''
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.
        '''
        self.query = Queries()

    def actualizar_fecha(self, calendario, fecha, variable, campo_texto):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.

        :param calendario: instancia de la clase Calendar_date.
        :type calendario: Calendar_date
        :param fecha: fecha seleccionada por el usuario.
        :type fecha: datetime
        :param variable: variable que se utiliza para almacenar la fecha seleccionada.
        :type variable: tk.StringVar
        :param campo_texto: caja de texto donde se muestra la fecha seleccionada.
        :type campo_texto: tk.Label

        """
        calendario = Calendar_date()
        calendario.mostrar_calendario()

        fecha = calendario.selected_datetime

        variable.set(fecha)

        # Elimina cualquier texto existente en la caja de texto
        campo_texto.config(text="")

        # Inserta el nuevo valor en la caja de texto
        campo_texto.config(text=fecha)



    def hacer_consulta_entrada(self, fecha_inicio_entrada:str, fecha_fin_entrada:str, fecha_inicio_salida:str, fecha_fin_salida:str, corte_numero:int, id:int) -> list:
        """
        Realiza una consulta SQL con los valores proporcionados por el usuario y devuelve una lista de registros obtenidos.

        Args:
        fecha_inicio_entrada (str): fecha de inicio de entrada en formato yyyy-mm-dd hh:mm:ss.
        fecha_fin_entrada (str): fecha de fin de entrada en formato yyyy-mm-dd hh:mm:ss.
        fecha_inicio_salida (str): fecha de inicio de salida en formato yyyy-mm-dd hh:mm:ss.
        fecha_fin_salida (str): fecha de fin de salida en formato yyyy-mm-dd hh:mm:ss.
        corte_numero (int): número de corte a consultar.
        id (int): ID del registro a consultar.

        Returns:
        list: una lista de registros obtenidos por la consulta.

        Raises:
        ValueError: si los campos para la consulta están vacíos.
        TypeError: si el formato de la fecha ingresada no es correcto o la fecha ingresada no es válida.
        """
        try:
            parametros = {}

            # Obtener los valores de los campos de consulta
            self.fecha_inicio_entrada = fecha_inicio_entrada
            self.fecha_fin_entrada = fecha_fin_entrada
            self.fecha_inicio_salida = fecha_inicio_salida
            self.fecha_fin_salida = fecha_fin_salida
            self.corte_numero = corte_numero
            self.id = id

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

            if corte_numero != '':parametros['corte_numero'] = int(corte_numero)

            if id != '':parametros['id'] = int(id)


            # Validar que se hayan proporcionado parámetros para la consulta
            if parametros == {}:raise ValueError('Error: los campos están vacíos')

            # Realizar la consulta y devolver la lista de registros obtenidos
            registros = self.query.hacer_consulta_sql_entradas(parametros)
            return registros

        except ValueError:
            messagebox.showwarning('Error', 'Por favor introduzca un dato válido para realizar la consulta.')
        except TypeError:
            messagebox.showwarning('Error', 'El formato de la fecha ingresada no es correcto o la fecha ingresada no es válida')



    def realizar_reporte(self, ver_tabla, registros):
        """
        Realiza un reporte de los registros obtenidos en una consulta y lo guarda en un archivo de Excel.

        Args:
            ver_tabla (str): el nombre de la tabla que se está consultando
            registros (list): una lista de tuplas que contiene los registros obtenidos de la consulta

        Raises:
            TypeError: Si no se ha realizado una consulta antes de generar un reporte.
            ValueError: Si la consulta está vacía y no se puede generar un reporte.
            AttributeError: Si hay valores inválidos en los campos Entrada o Salida para realizar la consulta.
            exceptions.FileCreateError: Si el archivo de Excel no se puede crear.
        """
        self.registros = registros

        try:
            # Verificar que se haya realizado una consulta antes de generar un reporte
            if self.registros is None: raise TypeError('Error: no se ha realizado una consulta antes de generar un reporte')
            if len(self.registros) == 0: raise ValueError('Error: la consulta esta vacia y no se puede generar un reporte')

            # Obtener la ruta y el nombre del archivo donde se guardará el reporte
            ruta_archivo = filedialog.asksaveasfilename(defaultextension='.xlsx', initialfile=f'reporte_')

            # Crear un archivo de Excel y escribir los registros
            workbook = xlsxwriter.Workbook(ruta_archivo, {'remove_timezone': True})
            worksheet = workbook.add_worksheet()

            # Obtener las columnas de la tabla
            columnas = self.query.obtener_campos_tabla(ver_tabla)

            # Establecer el nombre de las columnas en la primera fila
            for i in range(len(columnas)):
                worksheet.write(0, i, columnas[i])

            # Escribir los registros
            for i, registro in enumerate(self.registros):
                for j, valor in enumerate(registro):
                    # Si el campo es "Entrada" o "Salida", convertir a fecha y hora
                    if columnas[j] == 'Entrada' or columnas[j] == 'Salida':
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
            os.chmod(ruta_archivo, 0o777)
            messagebox.showinfo('Mensaje', 'El reporte fue generado con exito')

        #Manejo de errores
        except TypeError:messagebox.showerror('Error', 'Para realizar un reporte primero tiene que realizar una consulta')
        except ValueError:messagebox.showerror('Error', 'Para realizar un reporte primero tiene que realizar una consulta que contenga registros')
        except AttributeError:messagebox.showerror('Error', 'El reporte no se puede generar ya que en los campos Entrada o Salida hay valores invalidos para realizar la consulta, favor de revisar y volver a intentar')
        except exceptions.FileCreateError:messagebox.showerror('Error', 'El reporte no se puede generar, seleccione el directorio para guardar el reporte y vuelva a intentar')

