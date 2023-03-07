import pymysql
import xlwt
try:

	conexion = pymysql.connect(host='localhost',
                             user='Aurelio',
                             password='RG980320',
                             db='Parqueadero1')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT id, Entrada, Salida FROM Entradas;")
 
			# Con fetchall traemos todas las filas
			Entradas = cursor.fetchall()
 
			# Recorrer e imprimir
			fmt = xlwt.easyxf

			encabezado = fmt('font: name Arial, color red, bold on;')
			centrado = fmt('alignment: horiz centre')

			wb = xlwt.Workbook()

			full = wb.add_sheet("Paa 1")

			full.write(0, 0, "id", encabezado)
			full.write(0, 1, "Entrada", encabezado)
			full.write(0, 2, "Salida", encabezado)
			for fila in Entradas:
							print(Entradas)
							print(fila[0],'/n')
							full.write(fila[0], 0, fila[0],centrado)
							full.write(fila[0], 1, str(fila[1]),centrado)
							full.write(fila[0], 2, str(fila[2]),centrado)
				            #full.write(fila[0], 2, fila[2]) #marca errorpor que el valor es NONE, y no puede aplicar el formato al campo vacio, segun entiendo
				#full.write(x, 3, "=",centrado)
				#full.write(x, 4, xlwt.Formula('A%s*C%s' % (x+1, x+1)))
							wb.save('Consulta.xls')	
				
				
				
				
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
	


# ~ for x in range(1, 11):
		# ~ full.write(x, 0, 5,centrado)
		# ~ full.write(x, 1, "x",centrado)
		# ~ full.write(x, 2, x,centrado)
		# ~ full.write(x, 3, "=",centrado)
		# ~ full.write(x, 4, xlwt.Formula('A%s*C%s' % (x+1, x+1)))

# ~ wb.save('Tabla_5.xls')
	
	
