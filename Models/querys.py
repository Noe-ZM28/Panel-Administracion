from database import database_connection


class Querys:
    def __init__ (self, data_base = None):
        self.data_base = database_connection()


    def obtener_campos_tabla(self, tabla):
        query = f"DESCRIBE {tabla}"
        resultado = self.data_base.execute_query(query)
        campos = [r[0] for r in resultado]
        return campos

consulta = Querys()
print(consulta.obtener_campos_tabla('Usuarios'))



