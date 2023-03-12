import tkinter as tk

class ControllerLogin:
    def __init__(self):
        pass


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

            # Imprime los datos en la consola
            print(f'Tema: {self.theme}')
            print(f'Usuario: {self.user}')
            print(f'Contraseña: {self.password}')
        except TypeError as e:
            # Si se lanza una excepción TypeError, muestra un mensaje de error en una ventana de diálogo
            tk.messagebox.showerror('Error', f'Error: {e}')
