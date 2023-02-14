from database import database_connection as db


# database = db(host="187.131.147.109",
#     user="Aurelio",
#     password="RG980320",
#     database="Parqueadero1")
data_base = db(
                host="localhost",
                user="root",
                password="",
                database="db")


a = data_base.execute_query("SELECT * FROM Usuarios")
for row in a:
     print(row)
