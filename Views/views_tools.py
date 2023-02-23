from tkinter import *
from tkcalendar import *
from datetime import datetime
from datetime import date


class Calendar:

    def __init__(self):
        """
        Inicializa la clase Fecha_Hora, crea una ventana de Tkinter y los widgets necesarios para seleccionar una fecha y hora.
        """
        root = Toplevel()
        self.master = root
        self.master.title("Seleccionar fecha y hora")
        self.master.geometry("300x360")
        self.master.resizable(width=False, height=False)

        # Creamos variables de cadena para los campos de hora, minutos y segundos
        self.hour = IntVar()
        self.min = IntVar()
        self.sec = IntVar()

        # Almacena la fecha y hora seleccionada
        self.selected_datetime = ""

        # Fuente para los widgets
        f = ('Times', 20)

        # Creamos dos marcos para colocar los widgets
        self.fone = Frame(self.master)
        self.ftwo = Frame(self.master)

        self.fone.pack(pady=10)
        self.ftwo.pack(pady=10)

        # Creamos un calendario para seleccionar una fecha
        self.cal = Calendar(self.fone,
                            selectmode="day",
                            locale="es_ES",
                            year=date.today().year,
                            month=date.today().month,
                            day=date.today().day)
        self.cal.pack()

        # Creamos tres cuadros de entrada de tipo Spinbox para seleccionar la hora, minutos y segundos
        self.hour = Spinbox(self.ftwo, from_=0, to=23, wrap=True, textvariable=self.hour, width=2, state="readonly", font=f, justify=CENTER)

        self.min = Spinbox(self.ftwo, from_=0, to=59, wrap=True, textvariable=self.min, font=f, width=2, justify=CENTER)

        self.sec = Spinbox(self.ftwo,from_=0, to=59, wrap=True, textvariable=self.sec, width=2, font=f, justify=CENTER)

        # Añadimos los cuadros de entrada a la ventana
        self.hour.pack(side=LEFT, fill=X, expand=True)
        self.min.pack(side=LEFT, fill=X, expand=True)
        self.sec.pack(side=LEFT, fill=X, expand=True)

        # Etiqueta que indica la función de los cuadros de entrada
        self.msg = Label(self.master, text="Hora  Minuto  Segundo", font=("Times", 12))
        self.msg.pack(side=TOP)

        # Botón que llama a la función select_datetime() al hacer clic
        self.actionBtn = Button(self.master, text="Selecciona fecha y hora", padx=10, pady=10, command=self.select_datetime)
        self.actionBtn.pack(pady=10)


    def mostrar_calendario(self):
        self.master.mainloop()
        #self.master.wait_window()


    def salir_calendario(self):
        #detener el loop principal
        self.master.quit()
        # Destruye el panel principal
        self.master.destroy()


    def get_selected_datetime(self):
        return self.selected_datetime


    def format_datetime(self, date, hour, minute, second):
        """
        Función que da formato a la fecha y hora seleccionada.

        Args:
            date (str): Cadena que representa la fecha en formato dd/mm/aa.
            hour (int): Hora seleccionada en formato de 24 horas.
            minute (int): Minutos seleccionados.
            second (int): Segundos seleccionados.

        Returns:
            str: Cadena que representa la fecha y hora seleccionada en formato
            YYYY-MM-DD HH:MM:SS.
        """
        date_obj = datetime.strptime(date, "%d/%m/%y")
        date_str = date_obj.strftime("%Y-%m-%d")

        time_str = f"{hour:02}:{minute:02}:{second:02}"
        return f"{date_str} {time_str}"


    def select_datetime(self):
        """
        Función que guarda la fecha y hora seleccionada.

        Obtiene la fecha seleccionada en el calendario y la hora, minutos y segundos
        seleccionados en los Spinboxes. Luego, utiliza la función format_datetime
        para dar formato a la fecha y hora seleccionada y guarda el resultado en
        el atributo selected_datetime.

        """
        date = self.cal.get_date()
        hour = int(self.hour.get())
        minute = int(self.min.get())
        second = int(self.sec.get())

        # Dar formato a la fecha y hora seleccionada
        self.selected_datetime = self.format_datetime(date, hour, minute, second)
        # print(self.selected_datetime)

        # Destruir la ventana principal
        self.salir_calendario()

