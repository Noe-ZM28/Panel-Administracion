from Views.view_panel_administracion import View_Panel_Administracion
from tkinter import messagebox


class Controller_Select_Conection:
    pass
    def __init__(self) -> None:
        self.conexion = ''

    def conectar(self, estacionamiento):
        try: 
            self.estacionamiento = estacionamiento

            if self.estacionamiento == 'Conexion Prueba':self.conexion = 'Configuracion prueba-1'

            elif self.estacionamiento == 'Ciudad Mendoza':self.conexion = 'Configuracion CiudadMendoza'
            elif self.estacionamiento == 'Durango':self.conexion = 'Configuracion Durango'
            elif self.estacionamiento == 'Monterrey':self.conexion = 'Configuracion Monterrey'
            elif self.estacionamiento == 'Pino Suarez':self.conexion = 'Configuracion PinoSuarez'
            elif self.estacionamiento == 'Tenayuca':self.conexion = 'Configuracion Tenayuca'

            else:raise TypeError(f'Conexion desconocida: {self.estacionamiento}.')

            print(f'conectado a -> #{self.estacionamiento}#')
            self.panel_administracion = View_Panel_Administracion(estacionamiento = self.conexion)

        except TypeError as e:
            messagebox.showwarning("Error", f"{e} ")
            return None


