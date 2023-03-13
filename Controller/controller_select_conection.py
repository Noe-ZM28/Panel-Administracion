from Views.view_panel_administracion import View_Panel_Administracion
from tkinter import messagebox


class Controller_Select_Conection:
    """
    Controlador para seleccionar la conexión a una base de datos.
    """
    def __init__(self) -> None:
        #Inicializa la variable de conexión a una cadena vacía.
        self.conexion = ''

    def conectar(self, estacionamiento):
        """
        Conecta con la base de datos correspondiente según la opción seleccionada por el usuario.

        Parámetros:
        - estacionamiento (str): el nombre del estacionamiento seleccionado por el usuario.

        Retorna:
        - None si se produce un error.
        """
        try:
            # Asigna el valor de estacionamiento a la variable correspondiente
            self.estacionamiento = estacionamiento

            # Asigna la configuración de conexión correspondiente según el estacionamiento seleccionado
            if self.estacionamiento == 'Conexion Prueba':self.conexion = 'Configuracion prueba-1'

            elif self.estacionamiento == 'Ciudad Mendoza':self.conexion = 'Configuracion CiudadMendoza'
            elif self.estacionamiento == 'Durango': self.conexion = 'Configuracion Durango'
            elif self.estacionamiento == 'Monterrey':self.conexion = 'Configuracion Monterrey'
            elif self.estacionamiento == 'Pino Suarez':self.conexion = 'Configuracion PinoSuarez'
            elif self.estacionamiento == 'Tenayuca':self.conexion = 'Configuracion Tenayuca'

            # Si el estacionamiento seleccionado no es válido, lanza una excepción TypeError
            else:raise TypeError(f'Conexión desconocida: {self.estacionamiento}.')

            # Crea una instancia de View_Panel_Administracion con la configuración de conexión correspondiente
            self.panel_administracion = View_Panel_Administracion(estacionamiento=self.conexion)
            print(f'Conectado a -> {self.estacionamiento}')

        except TypeError as e:
            # Si se produce una excepción TypeError, muestra un mensaje de advertencia y retorna None
            messagebox.showwarning("Error", f"{e} ")
            return None

