from Models.database import database_connection

class SelectController:
    pass
    def __init__(self) -> None:
        self.conection_database = database_connection()

    def conectar(self, estacionamiento):
        self.estacionamiento = estacionamiento
        print(f'#{self.estacionamiento}#')


        # if self.estacionamiento == 'Oficina Chiapas': 
        #     self.conection_database.connect('Configuracion 3')


        # elif self.estacionamiento == 'Ciudad Mendoza': pass
        # elif self.estacionamiento == 'Durango': pass
        # elif self.estacionamiento == 'Monterrey': pass
        # elif self.estacionamiento == 'Pino Suarez': pass
        # elif self.estacionamiento == 'Tenayuca': pass

        # else: print(f'Conexion desconocida: {self.estacionamiento}.')


