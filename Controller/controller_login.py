from Config.config_tools import tools
import tkinter as tk
import json


class ControllerLogin:
    def __init__(self):
        self.theme = None
        self.user = None
        self.password = None

        self.tools_instance = tools()
        self.user_settings_file = self.tools_instance.read_path_config_file('config_files',"user_settings_file")

    def get_data(self, theme=None, user=None, password=None):
        """
        Obtiene los datos de usuario y tema, y los imprime en la consola.
        """
        try:
            # Asigna los valores de tema, usuario y contraseña a las variables correspondientes
            self.theme = theme
            self.user = user
            self.password = password

            # Si el usuario o la contraseña están vacíos, lanza una excepción TypeError
            if user == '' or password == '':
                raise TypeError('El campo Usuario o Contraseña está vacío, no deje campos en blanco.')

            user_data = self.obtener_configuracion(UserName = self.user)
            self.compobar_usuario(user_data)

        except TypeError as e:
            # Si se lanza una excepción TypeError, muestra un mensaje de error en una ventana de diálogo
            tk.messagebox.showerror('Error', f'Error: {e}')


    def compobar_usuario(self, user_data = None):
        try:
            if user_data:
                if self.user == user_data['UserName'] and self.password == user_data['Password']:
                    print(f"Dentro!: {user_data['Name']} ")
                else: raise KeyError("El nombre de usuario o contraseña son incorrectos")

        except KeyError as e:
            # Si se lanza una excepción TypeError, muestra un mensaje de error en una ventana de diálogo
            tk.messagebox.showerror('Error', f"Error: {e}")


    def obtener_configuracion(self, UserName):
        """
        Obtiene los datos del usuario a partir de su nombre.

        Args: UserName (str): nombre del usuario

        Returns: dict: un diccionario con los parámetros de los usuarios.

        Raises: ValueError: si no se encuentra el usuario especificado.
        """
        try:
            with open(self.user_settings_file, "r") as f:
                data = json.load(f)

            # Obtiene la configuración seleccionada
            usuario = None
            for user in data["ussers"]:
                if user["UserName"] == UserName:
                    usuario = user
                    break

            if usuario is None:raise ValueError("El usuario ingresaste no está registrado")

            return usuario
        
         # Si se lanza una excepción TypeError, muestra un mensaje de error en una ventana de diálogo
        except ValueError as e:tk.messagebox.showerror('Error', f'Error: {e}')

            
