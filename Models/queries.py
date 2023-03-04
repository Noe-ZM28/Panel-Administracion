from tkinter import messagebox

from Models.database import database_connection



class Queries:
    """
    Esta clase contiene métodos para ejecutar consultas a una base de datos mediante una conexión establecida con la clase
    `database_connection`.
    """
    def __init__ (self, data_base = None):
        self.data_base = database_connection()

    def obtener_campos_tabla(self):
        """
        Obtiene los nombres de los campos en una tabla especificada.

        :param tabla: Nombre de la tabla.
        :return: Lista de los nombres de los campos en la tabla, excluyendo los campos "vobo" y "QRPromo".
        """
        query = f"DESCRIBE Entradas;"
        resultado = self.data_base.execute_query(query)
        exclusions = ["vobo", "QRPromo"]
        campos = [r[0] for r in resultado if r[0] not in exclusions]
        return campos

    def obtener_lista_de(self, listar, revez=None):
        """
        Devuelve una lista con los valores únicos de la columna especificada de la tabla 'Entradas' de la base de datos.

        Args:
        - listar: nombre de la columna de la tabla 'Entradas' de la que se quieren obtener los valores únicos.
        - revez: (opcional) si se especifica 'D', devuelve los valores en orden descendente; si se especifica 'A', los devuelve en orden ascendente; si no se especifica, los devuelve en el orden en que se encuentran en la tabla.

        return:
        - lista_sin_nones: una lista con los valores únicos de la columna especificada de la tabla 'Entradas', sin incluir valores 'None'.
        """
        # Si revez es igual a 'D', la consulta se hace en orden descendente.
        if revez == 'D': 
            query = f"SELECT DISTINCT {listar} FROM Entradas ORDER BY {listar} DESC;"
        # Si revez es igual a 'A', la consulta se hace en orden ascendente.
        elif revez == 'A': 
            query = f"SELECT DISTINCT {listar} FROM Entradas ORDER BY {listar} ASC;"
        # Si revez no está definido, se realiza una consulta simple.
        if revez == None: 
            query = f"SELECT DISTINCT {listar} FROM Entradas;" 

        # Se ejecuta la consulta y se obtiene el resultado.
        resultado = self.data_base.execute_query(query)
        # Se obtiene una lista con los valores de la columna especificada, sin valores None.
        lista = [r[0] for r in resultado]
        lista_sin_nones = list(filter(lambda x: x is not None, lista))
        # Se retorna la lista sin los valores None.
        return lista_sin_nones


    def obtener_registros_completos(self):
        """
        Obtiene todos los registros de una tabla especificada.

        :return: Todos los registros de la tabla.
        """
        query = f"SELECT id, Entrada, Salida, TiempoTotal, Importe, CorteInc, Placas, TarifaPreferente, TipoPromocion FROM Entradas;"
        print(query)
        registros = self.data_base.execute_query(query)
        return registros

    def hacer_consulta_sql_entradas(self, parametros):
        """
        Crea una consulta SQL dependiendo de los valores de los campos de consulta.

        Args:
        fecha_inicio_entrada (str): fecha de inicio en formato YYYY-MM-DD para entradas.
        fecha_fin_entrada (str): fecha de fin en formato YYYY-MM-DD para entradas.
        fecha_inicio_salida (str): fecha de inicio en formato YYYY-MM-DD para salidas.
        fecha_fin_salida (str): fecha de fin en formato YYYY-MM-DD para salidas.
        corte_numero (int): número de corte.
        id (int): número de id.

        Returns:
        str: consulta SQL.
        """

        # Creamos una lista vacía para agregar las cláusulas WHERE a nuestra consulta
        where = []
        ############################################################################################################################
        # Si existe el parámetro 'id' en el diccionario de parámetros,
        # se agrega una condición a la lista de condiciones a evaluar.
        if 'id' in parametros:where.append(f"id = {parametros['id']}")
        ############################################################################################################################

        ############################################################################################################################
        if 'tarifa' in parametros:where.append(f"TarifaPreferente = '{parametros['tarifa']}'")
        # Si existe el parámetro 'tarifa_preferente' en el diccionario de parámetros,
        # se agrega una condición a la lista de condiciones a evaluar.
        if 'tarifa_preferente' in parametros:
            if len(parametros['tarifa_preferente']) == 1:
                if  parametros['tarifa_preferente']:
                    where.append(f"TarifaPreferente = '{str(parametros['tarifa_preferente'][0])}'")
            else: #len(parametros['tarifa_preferente']) > 1:
                    where.append(f"TarifaPreferente IN {parametros['tarifa_preferente']}")
        ############################################################################################################################

        ############################################################################################################################
        # Si se especifica una fecha de inicio y una fecha de fin para entradas, agregamos una cláusula WHERE que seleccione
        # todas las entradas entre esas dos fechas. Si solo se especifica una fecha de inicio o una fecha de fin para entradas,
        # seleccionamos todas las entradas a partir de la fecha de inicio o hasta la fecha de fin, respectivamente.
        if 'fecha_inicio_entrada' in parametros and 'fecha_fin_entrada' in parametros:
            where.append(f"Entrada BETWEEN '{parametros['fecha_inicio_entrada']}' AND '{parametros['fecha_fin_entrada']}'")

        elif 'fecha_inicio_entrada' in parametros:where.append(f"Entrada >= '{parametros['fecha_inicio_entrada']}'")
        elif 'fecha_fin_entrada' in parametros:where.append(f"Entrada <= '{parametros['fecha_fin_entrada']}'")
        ##############################################################
        # Si se especifica una fecha de inicio y una fecha de fin para salidas, agregamos una cláusula WHERE que seleccione
        # todas las salidas entre esas dos fechas. Si solo se especifica una fecha de inicio o una fecha de fin para salidas,
        # seleccionamos todas las salidas a partir de la fecha de inicio o hasta la fecha de fin, respectivamente.
        if 'fecha_inicio_salida' in parametros and 'fecha_fin_salida' in parametros:
            where.append(f"Salida BETWEEN '{parametros['fecha_inicio_salida']}' AND '{parametros['fecha_fin_salida']}'")

        elif 'fecha_inicio_salida' in parametros:where.append(f"Salida >= '{parametros['fecha_inicio_salida']}'")
        elif  'fecha_fin_salida' in parametros:where.append(f"Salida <= '{parametros['fecha_fin_salida']}'")
        ############################################################################################################################

        ############################################################################################################################
        if 'tiempo_dentro' in parametros:
            # Si existe el parámetro 'tiempo_dentro' en el diccionario de parámetros,
            # se agrega una condición a la lista de condiciones a evaluar.
            where.append(f"TiempoTotal = '{str(parametros['tiempo_dentro'])}'")

        if 'tiempo_dentro_inicio' in parametros and 'tiempo_dentro_fin' in parametros:
            # Si existen los parámetros 'tiempo_dentro_inicio' y 'tiempo_dentro_fin'
            # en el diccionario de parámetros, se agrega una condición a la lista de
            # condiciones a evaluar.
            where.append(f"TiempoTotal BETWEEN '{str(parametros['tiempo_dentro_inicio'])}' AND '{str(parametros['tiempo_dentro_fin'])}'")

        elif 'tiempo_dentro_inicio' in parametros:
            # Si existe únicamente el parámetro 'tiempo_dentro_inicio' en el
            # diccionario de parámetros, se agrega una condición a la lista de
            # condiciones a evaluar.
            where.append(f"TiempoTotal >= '{str(parametros['tiempo_dentro_inicio'])}'")

        elif 'tiempo_dentro_fin' in parametros:
            # Si existe únicamente el parámetro 'tiempo_dentro_fin' en el
            # diccionario de parámetros, se agrega una condición a la lista de
            # condiciones a evaluar.
            where.append(f"TiempoTotal <= '{str(parametros['tiempo_dentro_fin'])}'")
        ############################################################################################################################

        ############################################################################################################################
        # Si se especifica el número de corte, agregamos una cláusula WHERE a la lista
        if 'corte_numero' in parametros:
            where.append(f"CorteInc = {parametros['corte_numero']}")

        # Si se especifican tanto el inicio como el fin del rango de números de corte,
        # agregamos una cláusula WHERE entre ellos
        if 'corte_numero_inicio' in parametros and 'corte_numero_fin' in parametros:
            where.append(f"CorteInc BETWEEN {parametros['corte_numero_inicio']} AND {parametros['corte_numero_fin']}")

        # Si solo se especifica el número de inicio del rango de números de corte, 
        # agregamos una cláusula WHERE para números de corte mayores o iguales a él
        elif 'corte_numero_inicio' in parametros:
            where.append(f"CorteInc >= {parametros['corte_numero_inicio']}")

        # Si solo se especifica el número de fin del rango de números de corte, 
        # agregamos una cláusula WHERE para números de corte menores o iguales a él
        elif 'corte_numero_fin' in parametros:
            where.append(f"CorteInc <= {parametros['corte_numero_fin']}")
        ############################################################################################################################

        ############################################################################################################################
        # Si se especifica el importe, agregamos una cláusula WHERE a la lista
        if 'ingreso' in parametros:
            where.append(f"Importe = '{parametros['ingreso']}'")

        # Si se especifica un rango de importes, agregamos una cláusula BETWEEN a la lista
        if 'ingreso_mayor' in parametros and 'ingreso_menor' in parametros:
            where.append(f"Importe BETWEEN '{parametros['ingreso_menor']}' AND '{parametros['ingreso_mayor']}'")

        # Si se especifica un importe máximo, agregamos una cláusula <= a la lista
        elif 'ingreso_mayor' in parametros:
            where.append(f"Importe <= '{parametros['ingreso_mayor']}'")

        # Si se especifica un importe mínimo, agregamos una cláusula >= a la lista
        elif 'ingreso_menor' in parametros:
            where.append(f"Importe >= '{parametros['ingreso_menor']}'")

        ############################################################################################################################

        ############################################################################################################################
        # Si existe el parámetro 'promocion' en el diccionario de parámetros,
        # se agrega una condición a la lista de condiciones a evaluar.
        if 'promocion' in parametros:where.append(f"TipoPromocion = '{parametros['promocion']}'")
        # Si existe el parámetro 'tipo_promocion' en el diccionario de parámetros,
        # se agrega una condición a la lista de condiciones a evaluar.
        if 'tipo_promocion' in parametros:
            if len(parametros['tipo_promocion']) == 1:
                if  parametros['tipo_promocion']:
                    where.append(f"TipoPromocion = '{str(parametros['tipo_promocion'][0])}'")
            else: #len(parametros['tipo_promocion']) > 1:
                    where.append(f"TipoPromocion IN {parametros['tipo_promocion']}")

        ############################################################################################################################

        ############################################################################################################################
        # Si tenemos al menos una cláusula WHERE, las unimos con el operador AND y agregamos la cláusula WHERE
        # completa a nuestra consulta SQL. De lo contrario, simplemente dejamos la cláusula WHERE vacía.
        if where:
            where_clause = "WHERE " + " AND ".join(where)
        else:
            where_clause = ""
        ############################################################################################################################
        
        # Devolvemos la consulta SQL completa
        query =  f"SELECT id, Entrada, Salida, TiempoTotal, Importe, CorteInc, Placas, TarifaPreferente, TipoPromocion FROM Entradas {where_clause};"
        print(query)
        registros = self.data_base.execute_query(query)

        if len(registros) == 0:
            messagebox.showinfo('Info', 'No hay registros que correspondan a la consulta establecida.')
        return registros


