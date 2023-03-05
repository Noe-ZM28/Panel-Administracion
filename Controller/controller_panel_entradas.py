from Views.views_tools import Calendar_date
from Models.queries import Queries
from Config.config_tools import tools

import PIL


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from tkinter import ttk


import xlsxwriter
from xlsxwriter import exceptions

from datetime import datetime

import os


class EntradasController:
    def __init__(self, theme = None):
        '''
        Constructor de la clase. Crea la ventana principal, la tabla y los campos de consulta.
        '''
        self.query = Queries()
        self.tools_instance = tools()
        self.theme = theme


    def actualizar_fecha(self, calendario, fecha, variable, campo_texto):
        """
        Actualiza la fecha y hora de inicio para la búsqueda de registros en la base de datos. 
        Utiliza un hilo para mostrar el calendario y obtener la fecha seleccionada por el usuario.

        :param calendario: instancia de la clase Calendar_date.
        :param fecha: fecha seleccionada por el usuario.
        :param variable: variable que se utiliza para almacenar la fecha seleccionada.
        :param campo_texto: caja de texto donde se muestra la fecha seleccionada.
        """
        calendario = Calendar_date(self.theme)
        calendario.mostrar_calendario()

        fecha = calendario.selected_datetime

        variable.set(fecha)

        # Elimina cualquier texto existente en la caja de texto
        campo_texto.config(text="")

        # Inserta el nuevo valor en la caja de texto
        campo_texto.config(text=fecha)


    def hacer_consulta_entrada(self, id:int, tarifa:str, tarifa_preferente:str, fecha_inicio_entrada:str, fecha_fin_entrada:str, fecha_inicio_salida:str, fecha_fin_salida:str, tiempo_dentro:str, tiempo_dentro_inicio:str, tiempo_dentro_fin:str, corte_numero:int, corte_numero_inicio:int, corte_numero_fin:int, ingreso:str, ingreso_mayor:str, ingreso_menor:str, tipo_promocion:str, promocion:str) -> list:
        """
        Realiza una consulta SQL con los valores proporcionados por el usuario y devuelve una lista de registros obtenidos.

        Args:
        id (int): ID del registro a consultar.
        tarifa (str): tarifa a consultar
        tarifa_preferente (str): valor de la tarifa preferente para consultar.
        fecha_inicio_entrada (str): fecha de inicio de entrada en formato yyyy-mm-dd hh:mm:ss para consultar.
        fecha_fin_entrada (str): fecha de fin de entrada en formato yyyy-mm-dd hh:mm:ss para consultar.
        fecha_inicio_salida (str): fecha de inicio de salida en formato yyyy-mm-dd hh:mm:ss para consultar.
        fecha_fin_salida (str): fecha de fin de salida en formato yyyy-mm-dd hh:mm:ss para consultar.
        tiempo_dentro (str): duración de tiempo dentro del estacionamiento en formato "hh:mm:ss" para consultar.
        tiempo_dentro_inicio (str): duración de tiempo dentro del estacionamiento en formato "hh:mm:ss" para consultar, con un rango de inicio.
        tiempo_dentro_fin (str): duración de tiempo dentro del estacionamiento en formato "hh:mm:ss" para consultar, con un rango final.
        corte_numero (int): número de corte a consultar.
        corte_numero_inicio (int): número de corte a consultar, con un rango de inicio.
        corte_numero_fin (int): número de corte a consultar, con un rango final.
        ingreso (str): valor de ingreso para consultar.
        ingreso_mayor (str): valor de ingreso mayor para consultar.
        ingreso_menor (str): valor de ingreso menor para consultar.
        tipo_promocion (str): tipo de promoción para consultar.
        tarifa (str): tarifa a consultar.

        Returns:
        list: una lista de registros obtenidos por la consulta.

        Raises:
        ValueError: si los campos para la consulta están vacíos.
        TypeError: si el dato ingresado no es válido.
        """

        try:
            parametros = {}

            # Obtener los valores de los campos de consulta
            self.id = id
            self.tarifa_preferente = tarifa_preferente


            self.fecha_inicio_entrada = fecha_inicio_entrada
            self.fecha_fin_entrada = fecha_fin_entrada
            self.fecha_inicio_salida = fecha_inicio_salida
            self.fecha_fin_salida = fecha_fin_salida

            self.tiempo_dentro = tiempo_dentro
            self.tiempo_dentro_inicio = tiempo_dentro_inicio
            self.tiempo_dentro_fin = tiempo_dentro_fin


            self.corte_numero = corte_numero
            self.corte_numero_inicio = corte_numero_inicio
            self.corte_numero_fin = corte_numero_fin

            self.ingreso = ingreso
            self.ingreso_mayor = ingreso_mayor
            self.ingreso_menor = ingreso_menor


            self.tipo_promocion = tipo_promocion
            self.promocion = promocion

            # Validar y agregar los parámetros a la consulta
            ##########################################################################################################
            if id != '': parametros['id'] = int(id)
            ##########################################################################################################

            ##########################################################################################################
            if tarifa != '': parametros['tarifa'] = str(tarifa)

            if tarifa_preferente != []: parametros['tarifa_preferente'] = tuple(tarifa_preferente)
            ##########################################################################################################

            ##########################################################################################################
            if fecha_inicio_entrada != '':
                if len(fecha_inicio_entrada) != 19:
                    raise ValueError('Error, La cantidad de caracteres no corresponde al formato de fecha')
                parametros['fecha_inicio_entrada'] = str(fecha_inicio_entrada)

            if fecha_fin_entrada != '':
                if len(fecha_fin_entrada) != 19:
                    raise ValueError('Error, La cantidad de caracteres no corresponde al formato de fecha')
                parametros['fecha_fin_entrada'] = str(fecha_fin_entrada)

            if 'fecha_inicio_entrada' in parametros and 'fecha_fin_entrada' in parametros:
                if parametros['fecha_inicio_entrada'] > parametros['fecha_fin_entrada']:
                    raise ValueError("La fecha de inicio debe ser menor o igual que la fecha final.")


            if fecha_inicio_salida != '':
                if len(fecha_inicio_salida) != 19:
                    raise ValueError('Error, La cantidad de caracteres no corresponde al formato de fecha')
                parametros['fecha_inicio_salida'] = str(fecha_inicio_salida)

            if fecha_fin_salida != '':
                if len(fecha_fin_salida) != 19:
                    raise ValueError('Error, La cantidad de caracteres no corresponde al formato de fecha')
                parametros['fecha_fin_salida'] = str(fecha_fin_salida)

            if 'fecha_inicio_salida' in parametros and 'fecha_fin_salida' in parametros:
                if parametros['fecha_inicio_salida'] > parametros['fecha_fin_salida']:
                    raise ValueError("La fecha de inicio debe ser menor o igual que la fecha final.")
            ##########################################################################################################

            ##########################################################################################################
            if tiempo_dentro != '' and tiempo_dentro != '0:0:00':
                parametros['tiempo_dentro'] = str(tiempo_dentro)

            if tiempo_dentro_inicio != '' and tiempo_dentro_inicio != '0:0:00':
                parametros['tiempo_dentro_inicio'] = str(tiempo_dentro_inicio)

            if tiempo_dentro_fin != '' and tiempo_dentro_fin != '0:0:00':
                parametros['tiempo_dentro_fin'] = str(tiempo_dentro_fin)

            if 'tiempo_dentro_inicio' in parametros and 'tiempo_dentro_fin' in parametros:
                if parametros['tiempo_dentro_inicio'] > parametros['tiempo_dentro_fin']:
                    raise ValueError("El tiempo de inicio debe ser menor o igual que el tiempo final.")
            ##########################################################################################################

            ##########################################################################################################
            if corte_numero != '':parametros['corte_numero'] = int(corte_numero)
            if corte_numero_inicio != '':parametros['corte_numero_inicio'] = int(corte_numero_inicio)
            if corte_numero_fin != '':parametros['corte_numero_fin'] = int(corte_numero_fin)

            if 'corte_numero_inicio' in parametros and 'corte_numero_fin' in parametros:
                if parametros['corte_numero_inicio'] > parametros['corte_numero_fin']:
                    raise ValueError("El corte de inicio debe ser menor o igual que el corte final.")
            ##########################################################################################################

            ##########################################################################################################
            if ingreso != '':parametros['ingreso'] = round(float(ingreso), 1)
            if ingreso_mayor != '':parametros['ingreso_mayor'] = round(float(ingreso_mayor), 1)
            if ingreso_menor != '':parametros['ingreso_menor'] = round(float(ingreso_menor), 1)

            if 'ingreso_mayor' in parametros and 'ingreso_menor' in parametros:
                if parametros['ingreso_menor'] > parametros['ingreso_mayor']:
                    raise ValueError("El ingreso menor debe de ser menor al ingreso mayor.")
            ##########################################################################################################

            ##########################################################################################################
            if promocion != '': parametros['promocion'] = str(promocion)

            if tipo_promocion != []: parametros['tipo_promocion'] = tuple(tipo_promocion)
            ##########################################################################################################

            #print(parametros)
            # Validar que se hayan proporcionado parámetros para la consulta
            if parametros == {}:raise ValueError('Los campos están vacíos')

            # Realizar la consulta y devolver la lista de registros obtenidos
            registros = self.query.hacer_consulta_sql_entradas(parametros)
            return registros, parametros


        except ValueError as e:
            messagebox.showwarning('Error', f'Error: {e}\nPor favor introduzca un dato válido para realizar la consulta.')
        except TypeError as e:
            messagebox.showwarning('Error', f'Error: {e}\nEl dato ingresado no es válido')


    def realizar_reporte(self, registros, parametros):
        """
        Realiza un reporte de los registros obtenidos en una consulta y lo guarda en un archivo de Excel.

        Args:
            registros (list): una lista de tuplas que contiene los registros obtenidos de la consulta

        Raises:
            TypeError: Si no se ha realizado una consulta antes de generar un reporte.
            ValueError: Si la consulta está vacía y no se puede generar un reporte.
            exceptions.FileCreateError: Si el archivo de Excel no se puede crear.
        """
        self.registros = registros
        self.parametros = parametros

        # Obtener las columnas de la tabla
        #columnas = self.query.obtener_campos_tabla()
        columnas = ['Folio', 'Entrada', 'Salida', 'Tiempo', 'Importe', 'N° Corte', 'Placas', 'Tarifa', 'Promocion']


        try:
            # Verificar que se haya realizado una consulta antes de generar un reporte
            if self.registros is None: raise TypeError('Primero genera una consulta antes de generar un reporte')
            if len(self.registros) == 0: raise ValueError('La consulta esta vacia y no se puede generar un reporte')

            # Obtener la ruta y el nombre del archivo donde se guardará el reporte
            ruta_archivo = filedialog.asksaveasfilename(defaultextension='.xlsx', initialfile=f'reporte_')

            # Crear un archivo de Excel y escribir los registros
            workbook = xlsxwriter.Workbook(ruta_archivo, {'remove_timezone': True})
            worksheet = workbook.add_worksheet('Reporte')


            # Agregar la imagen en la esquina superior izquierda de la hoja de Excel
            imagen_path = self.tools_instance.read_path_config_file('images', 'logo_pase')
            imagen = PIL.Image.open(imagen_path)
            imagen_width, imagen_height = imagen.size

            worksheet.insert_image(0, 0, imagen_path, {'x_offset': 0, 'y_offset': 0, 'x_scale': 1, 'y_scale': 1})

            formato_columnas = workbook.add_format({'bold': True, 'align':'center', 'text_wrap':True, 'border':1, 'pattern':1, 'bg_color':'#D9D9D9'})
            formato_celdas_texto = workbook.add_format( {'bold': False, 'text_wrap':True, 'border':1, 'pattern':1,'bg_color':'white'})
            formato_celdas_moneda = workbook.add_format({'num_format': '$#,##0.00', 'bold': False, 'text_wrap':True, 'border':1, 'pattern':1,'bg_color':'white'})

            # Escribe los parámetros en la hoja de cálculo
            ultima_fila = 3
            for i, (clave, valor) in enumerate(self.parametros.items()):
                fila = i + 4
                worksheet.write(fila, 3, clave)
                if isinstance(valor, tuple):
                    for j, elem in enumerate(valor):
                        worksheet.write(fila, 4+j, elem)
                else:
                    worksheet.write(fila, 4, valor)
                ultima_fila = fila

            # Guarda el número de la última fila después de haber escrito los parámetros
            ultima_fila = worksheet.dim_rowmax
            print(ultima_fila)

            FILA_INICIO = ultima_fila + 3

            # Establecer el nombre y ancho de las columnas en función del contenido
            for i, columna in enumerate(columnas):
                worksheet.write(FILA_INICIO - 1, i, columnas[i], formato_columnas)
                max_longitud = max([len(str(registro[i])) for registro in self.registros] + [len(columna)]) + 1
                worksheet.set_column(i, i, max_longitud)

            #Establece el tamaño del campo tiempo a 8
            worksheet.set_column(3, 3, 8)


            # Escribir los registros
            for i, registro in enumerate(self.registros):
                for j, valor in enumerate(registro):
                    # Si el campo es "Entrada" o "Salida", convertir a fecha y hora
                    if columnas[j] == 'Entrada' or columnas[j] == 'Salida':
                        fecha_hora = datetime.strptime(valor.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
                        fecha_hora_str = datetime.strftime(fecha_hora, '%Y-%m-%d %H:%M:%S')

                        worksheet.write(i + FILA_INICIO, j, fecha_hora_str, formato_celdas_texto)

                    # Si el campo es "Importe", aplicar el formato de moneda
                    elif columnas[j] == 'Importe':
                        worksheet.write(i + FILA_INICIO, j, valor, formato_celdas_moneda)

                    else:
                        worksheet.write(i + FILA_INICIO, j, valor, formato_celdas_texto)


            suma_importe = sum(registro[columnas.index('Importe')] for registro in self.registros)

            worksheet.write('B7', 'Total de ingresos:')
            # Escribir la suma en la hoja de cálculo
            worksheet.write('C7', suma_importe, formato_celdas_moneda)

            # Cerrar el archivo de Excel
            workbook.close()
            os.chmod(ruta_archivo, 0o777)
            messagebox.showinfo('Mensaje', 'El reporte fue generado con exito')

        #Manejo de errores
        except TypeError as e:messagebox.showerror('Error', f'Error: {e}\nPara realizar un reporte primero tiene que realizar una consulta')
        except ValueError as e:messagebox.showerror('Error', f'Error: {e}\nPara realizar un reporte primero tiene que realizar una consulta que contenga registros')
        except exceptions.FileCreateError as e:messagebox.showerror('Error', f'Error: El reporte no se puede generar, seleccione el directorio para guardar el reporte y vuelva a intentar')

    def format_datetime(self, hour, minute):
        """
        Función que da formato a hora seleccionada.

        Args:
            hour (int): Hora seleccionada en formato de 24 horas.
            minute (int): Minutos seleccionados.
            second (int): Segundos seleccionados.

        Returns:
            str: Cadena que representa hora seleccionada en formato HH:MM:SS.
        """
        time_str = f"{hour:01}:{minute:02}:00"
        return time_str
