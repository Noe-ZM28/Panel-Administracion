from Views.view_panel_administracion import View_Panel_Administracion
from tkinter import messagebox


class Controller_Select_Conection:
    """
    Controlador para seleccionar la conexión a una base de datos.
    """
    def __init__(self) -> None:
        #Inicializa la variable de conexión a una cadena vacía.
        self.conexion = ''

    def conectar(self, estacionamiento, user_name):
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
            self.user_name = user_name

            # Asigna la configuración de conexión correspondiente según el estacionamiento seleccionado
            if self.estacionamiento == 'Conexion Prueba':self.conexion = 'Configuracion prueba-1'

            elif self.estacionamiento == 'Ciudad Mendoza':self.conexion = 'CiudadMendoza'
            elif self.estacionamiento == 'Durango': self.conexion = 'Durango'
            elif self.estacionamiento == 'Monterrey':self.conexion = 'Monterrey'
            elif self.estacionamiento == 'Pino Suarez':self.conexion = 'PinoSuarez'
            elif self.estacionamiento == 'Tenayuca':self.conexion = 'Tenayuca'

            # Si el estacionamiento seleccionado no es válido, lanza una excepción TypeError
            else:raise TypeError(f'Conexión desconocida: {self.estacionamiento}.')

            # Crea una instancia de View_Panel_Administracion con la configuración de conexión correspondiente
            self.panel_administracion = View_Panel_Administracion(
                                                                    estacionamiento=self.conexion,
                                                                    user_name= self.user_name)
            print(f'Conectado a -> {self.estacionamiento}')

        except TypeError as e:
            # Si se produce una excepción TypeError, muestra un mensaje de advertencia y retorna None
            messagebox.showwarning("Error", f"{e} ")
            return None

