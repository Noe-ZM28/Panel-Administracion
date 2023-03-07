# import the modules
from pymysql import*
import xlwt
import pandas.io.sql as sql

# connect the mysql with the python
con=connect(user="Aurelio",password="RG980320",host="localhost",database="Parqueadero1")

# read the data
df=sql.read_sql('select * from Entradas',con)

# print the data
print(df)

# export the data into the excel sheet
df.to_excel('ds.xls')

        # ~ conexion=pymysql.connect(host="localhost",
                                 # ~ user="Aurelio",
                                 # ~ passwd="RG980320",
                                 # ~ database="Parqueadero1")

        # ~ #conexion = pymysql.connect(host="192.168.1.91",
        # ~ #                   user="Aurelio",
        # ~ #                   passwd="RG980320",
        # ~ #                   database="Parqueadero1")
        # ~ return conexion
