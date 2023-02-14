import pymysql

class database_connection:
    """
    Esta clase permite la conexión a una base de datos MySQL específica.
    Incluye métodos para conectarse a la base de datos, cerrar la conexión y ejecutar consultas en la base de datos.
    """

    def __init__ (self, host: str, user: str, password: str, database: str):
        """
        Inicializa los atributos para la conexión a la base de datos.

        :param host: La dirección del host donde se encuentra la base de datos.
        :param user: El nombre de usuario con permisos para conectarse a la base de datos.
        :param password: La contraseña del usuario.
        :param database: El nombre de la base de datos a la que se desea conectar.
        """

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        """
        Realiza la conexión a la base de datos de MySQL con los parámetros especificados en el inicio de la clase.
        Asigna el objeto de conexión a una variable de instancia `connection`.
        """
        self.connection = pymysql.connect(
                                            host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            database=self.database)

    def close_connection(self):
        """
        Cierra la conexión con la base de datos.
        """
        self.connection.close()


    def execute_query(self, query: str, values = None):
        """
        Ejecuta una consulta en la base de datos.

        :param query: Consulta SQL a ejecutar.
        :param values: Valores a ser utilizados en la consulta.
        """
        cursor = self.connection.cursor()
        # Si se pasaron valores, se ejecuta la consulta con esos valores
        if values is not None:
            cursor.execute(query, values)

        # Si no se pasaron valores, se ejecuta la consulta sin ellos
        else:
            cursor.execute(query)

        result = cursor.fetchall()    
        self.connection.commit()
        cursor.close()
        #self.close_connection()

        return result

