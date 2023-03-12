import tkinter as tk

class ControllerLogin:
    def __init__(self) -> None:
        pass


    def get_data(self, theme = None, usser = None,password = None):
        try: 
            self.theme = theme
            self.usser = usser
            self.password = password

            if usser == '' or password == '': raise TypeError('El campo Usuario o Contraseña esta vacio, no deje campos en blanco.')

            print(f'Tema: {self.theme}')
            print(f'Usuario: {self.usser}')
            print(f'Contraseña: {self.password}')
        except TypeError as e:tk.messagebox.showerror('Error', f'Error: {e}')
