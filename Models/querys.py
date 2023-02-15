from database import database_connection as db

data_base = db()

class Querys:
    def obtener_campos_tabla(self, tabla):
        query = f"DESCRIBE {tabla}"
        resultado = data_base.execute_query(query)
        campos = [r[0] for r in resultado]
        return campos

consulta = Querys()
print(consulta.obtener_campos_tabla('Usuarios'))



