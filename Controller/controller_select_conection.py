from Models.database import database_connection
from Views.view_panel_administracion import View_Panel_Administracion

class Controller_Select_Conection:
    pass
    def __init__(self) -> None:
        self.conexion = ''

    def conectar(self, estacionamiento):
        self.estacionamiento = estacionamiento

        if self.estacionamiento == 'conexion prueba':self.conexion = 'Configuracion prueba'

        elif self.estacionamiento == 'Ciudad Mendoza':self.conexion = 'Configuracion CiudadMendoza'
        elif self.estacionamiento == 'Durango':self.conexion = 'Configuracion Durango'
        elif self.estacionamiento == 'Monterrey':self.conexion = 'Configuracion Monterrey'
        elif self.estacionamiento == 'Pino Suarez':self.conexion = 'Configuracion PinoSuarez'
        elif self.estacionamiento == 'Tenayuca':self.conexion = 'Configuracion Tenayuca'


        else:raise TypeError(f'Conexion desconocida: {self.estacionamiento}.')

        print(f'conectado a -> #{self.estacionamiento}#')
        View_Panel_Administracion(estacionamiento = self.conexion)

