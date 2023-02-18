from tkinter import messagebox

from Models.database import database_connection



class Queries:
    """
    Esta clase contiene métodos para ejecutar consultas a una base de datos mediante una conexión establecida con la clase
    `database_connection`.
    """
    def __init__ (self, data_base = None):
        self.data_base = database_connection()

    def obtener_campos_tabla(self, tabla):
        """
        Obtiene los nombres de los campos en una tabla especificada.

        :param tabla: Nombre de la tabla.
        :return: Lista de los nombres de los campos en la tabla.
        """
        query = f"DESCRIBE {tabla}"
        resultado = self.data_base.execute_query(query)
        campos = [r[0] for r in resultado]
        return list(campos)

    def obtener_registros(self, table):
        """
        Obtiene todos los registros de una tabla especificada.

        :param table: Nombre de la tabla.
        :return: Todos los registros de la tabla.
        """
        query = f"select * from {table};"
        registros = self.data_base.execute_query(query)
        return registros

    def obtener_registros_corte_numero(self, table, corte):
        query = f"select * from {table} WHERE CorteInc = {corte};"
        registros = self.data_base.execute_query(query)
        return registros


    def hacer_consulta_sql_entradas(self, parametros):#self, fecha_inicio_entrada = None, fecha_fin_entrada = None, fecha_inicio_salida = None, fecha_fin_salida = None, corte_numero = None, id = None):
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

        # Si se especifica el número de corte, agregamos una cláusula WHERE a la lista
        if 'corte_numero' in parametros:
            where.append(f"CorteInc = {parametros['corte_numero']}")

        # Si se especifica una fecha de inicio y una fecha de fin para entradas, agregamos una cláusula WHERE que seleccione
        # todas las entradas entre esas dos fechas. Si solo se especifica una fecha de inicio o una fecha de fin para entradas,
        # seleccionamos todas las entradas a partir de la fecha de inicio o hasta la fecha de fin, respectivamente.
        if 'fecha_inicio_entrada' in parametros and 'fecha_fin_entrada' in parametros:
            where.append(f"Entrada BETWEEN '{parametros['fecha_inicio_entrada']}' AND '{parametros['fecha_fin_entrada']}'")

        elif 'fecha_inicio_entrada' in parametros:
            where.append(f"Entrada >= '{parametros['fecha_inicio_entrada']}'")

        elif 'fecha_fin_entrada' in parametros:
            where.append(f"Entrada <= '{parametros['fecha_fin_entrada']}'")

        # Si se especifica una fecha de inicio y una fecha de fin para salidas, agregamos una cláusula WHERE que seleccione
        # todas las salidas entre esas dos fechas. Si solo se especifica una fecha de inicio o una fecha de fin para salidas,
        # seleccionamos todas las salidas a partir de la fecha de inicio o hasta la fecha de fin, respectivamente.
        if 'fecha_inicio_salida' in parametros and 'fecha_fin_salida' in parametros:
            where.append(f"Salida BETWEEN '{parametros['fecha_inicio_salida']}' AND '{parametros['fecha_fin_salida']}'")

        elif 'fecha_inicio_salida' in parametros:
            where.append(f"Salida >= '{parametros['fecha_inicio_salida']}'")
        elif  'fecha_fin_salida' in parametros:
            where.append(f"Salida <= '{parametros['fecha_fin_salida']}'")

        # Si se especifica un número de ID, agregamos una cláusula WHERE a la lista
        if 'id' in parametros:
            where.append(f"id = {parametros['id']}")

        # Si tenemos al menos una cláusula WHERE, las unimos con el operador AND y agregamos la cláusula WHERE
        # completa a nuestra consulta SQL. De lo contrario, simplemente dejamos la cláusula WHERE vacía.
        if where:
            where_clause = "WHERE " + " AND ".join(where)
        else:
            where_clause = ""

        # Devolvemos la consulta SQL completa
        query =  f"SELECT * FROM Entradas {where_clause};"
        print(query)
        registros = self.data_base.execute_query(query)
        return registros


        # if corte_numero == "" or 0: corte_numero == None
        # if id == "" or 0: id == None
        # if fecha_inicio_entrada == "" or 0: fecha_inicio_entrada == None
        # if fecha_fin_entrada == "" or 0: fecha_fin_entrada == None
        # if fecha_inicio_salida == "" or 0: fecha_inicio_salida == None
        # if fecha_fin_salida == "" or 0: fecha_fin_salida == None
