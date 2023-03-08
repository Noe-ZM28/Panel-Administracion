import pymysql
try:
	#######################
	
	   # ~ def abrir(self):
        # ~ conexion=pymysql.connect(host="localhost",
                                 # ~ user="Aurelio",
                                 # ~ passwd="RG980320",
                                 # ~ database="Parqueadero1")

        # ~ #conexion = pymysql.connect(host="192.168.1.91",
        # ~ #                   user="Aurelio",
        # ~ #                   passwd="RG980320",
        # ~ #                   database="Parqueadero1")
        # ~ return conexion
	#######################
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
			for Entradas in Entradas:
				print(Entradas)
				print('solo la fila 0 es : ',Entradas[0])
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)
