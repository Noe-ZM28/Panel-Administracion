from tkinter import *
from tkcalendar import *
from datetime import datetime
from datetime import date

class Fecha_Hora:

    def __init__(self):
        """
        Inicializa la clase Fecha_Hora, crea una ventana de Tkinter y los widgets necesarios para seleccionar una fecha y hora.
        """
        root = Tk()
        self.master = root
        self.master.title("Seleccionar fecha y hora")
        self.master.geometry("300x360")
        self.master.resizable(width=False, height=False)

        # Creamos variables de cadena para los campos de hora, minutos y segundos
        self.hour_string = StringVar()
        self.min_string = StringVar()
        self.sec_string = StringVar()

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
        self.min_sb = Spinbox(self.ftwo,
                              from_=0,
                              to=23,
                              wrap=True,
                              textvariable=self.hour_string,
                              width=2,
                              state="readonly",
                              font=f,
                              justify=CENTER)
        self.sec_hour = Spinbox(self.ftwo,
                                from_=0,
                                to=59,
                                wrap=True,
                                textvariable=self.min_string,
                                font=f,
                                width=2,
                                justify=CENTER)

        self.sec = Spinbox(self.ftwo,
                           from_=0,
                           to=59,
                           wrap=True,
                           textvariable=self.sec_string,
                           width=2,
                           font=f,
                           justify=CENTER)

        # Añadimos los cuadros de entrada a la ventana
        self.min_sb.pack(side=LEFT, fill=X, expand=True)
        self.sec_hour.pack(side=LEFT, fill=X, expand=True)
        self.sec.pack(side=LEFT, fill=X, expand=True)

        # Etiqueta que indica la función de los cuadros de entrada
        self.msg = Label(self.master,
                         text="Hora  Minuto  Segundo",
                         font=("Times", 12))
        self.msg.pack(side=TOP)

        # Botón que llama a la función select_datetime() al hacer clic
        self.actionBtn = Button(self.master,
                                text="Selecciona fecha y hora",
                                padx=10,
                                pady=10,
                                command=self.select_datetime)
        self.actionBtn.pack(pady=10)

        self.master.mainloop()

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
            dd-mm-aaaa hh:mm:ss.
        """
        date_obj = datetime.strptime(date, "%d/%m/%y")
        date_str = date_obj.strftime("%d-%m-%Y")

        time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
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
        hour = int(self.hour_string.get())
        minute = int(self.min_string.get())
        second = int(self.sec_string.get())

        # Dar formato a la fecha y hora seleccionada
        self.selected_datetime = self.format_datetime(date, hour, minute, second)

        # Destruir la ventana principal
        self.master.destroy()
