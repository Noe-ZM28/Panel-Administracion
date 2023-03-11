from Models.database import database_connection
from Views.view_panel_administracion import View_Panel_Administracion

class Controller_Select_Conection:
    pass
    def __init__(self) -> None:
        pass

    def conectar(self, estacionamiento):
        self.estacionamiento = estacionamiento

        if self.estacionamiento == 'Oficina Chiapas': 
            #self.conection_database.connect('Configuracion 3')
            View_Panel_Administracion(estacionamiento = 'Configuracion 1')

            print(f'#{self.estacionamiento}#')

        # elif self.estacionamiento == 'Ciudad Mendoza': pass
        # elif self.estacionamiento == 'Durango': pass
        # elif self.estacionamiento == 'Monterrey': pass
        # elif self.estacionamiento == 'Pino Suarez': pass
        # elif self.estacionamiento == 'Tenayuca': pass

        # else: print(f'Conexion desconocida: {self.estacionamiento}.')


