from database import database_connection as db

data_base = db(
                host="localhost",
                user="root",
                password="",
                database="db")


class Querys:
     def __init__():
          pass
     def obtener_campos_tabla(self, campo):
          query = "PRAGMA table_info({self.campo})"
          db.execute_query(self, query, campo)

# database = db(host="187.131.147.109",
#     user="Aurelio",
#     password="RG980320",
#     database="Parqueadero1")



a = data_base.execute_query("SELECT * FROM Usuarios")
for row in a:
     print(row)
