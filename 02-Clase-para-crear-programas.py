from tkinter import *
import os


class Programa:

    def __init__(self):
        self.ventana = ""
        self.titulo = "Programa1"
        self.icon = './imagenes/camara.ico'
        self.icon_alt = './APRENDER-TKINTER/imagenes/camara.ico'
        self.size = "770x470"
        self.resizable = True
        self.minsize = "400x200"  # Tamaño mínimo
        self.maxsize = "1024x800"  # Tamaño máximo

    def centrar_ventana(self, ventana, size):
        # Obtener el ancho y alto especificados en el formato "ancho x alto"
        ancho, alto = map(int, size.split("x"))

        # Obtener el tamaño de la pantalla
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()

        # Calcular la posición centrada
        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2

        # Configurar la geometría de la ventana
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def iniciar_programa(self):

        # Inicializar tkinter
        ventana = Tk()

        self.ventana = ventana

        # Añadiendo el título o nombre del programa
        self.ventana.title(self.titulo)

        # Centrar la ventana
        self.centrar_ventana(self.ventana, self.size)

        # Mostrar un icono o imágenes para el programa
        rutaimagen = os.path.abspath(self.icon)
        if not os.path.isfile(rutaimagen):
            rutaimagen = os.path.abspath(self.icon_alt)
        self.ventana.iconbitmap(rutaimagen)

        # Configurar si la ventana será redimensionable o no
        if self.resizable:
            self.ventana.resizable(1, 1)
        else:
            self.ventana.resizable(0, 0)

        # Configurar el tamaño mínimo y máximo
        min_ancho, min_alto = map(int, self.minsize.split("x"))
        max_ancho, max_alto = map(int, self.maxsize.split("x"))
        self.ventana.minsize(min_ancho, min_alto)
        self.ventana.maxsize(max_ancho, max_alto)

        # Configurar color de la ventana
        self.ventana.configure(bg="light blue")

        # Configurar atributos para la ventana
        self.ventana.attributes("-alpha", 1)  # Esta función permite configurar ciertos atributos como opacidad

    def cargar_texto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.config(
            height=10,
            width=50,
            fg="blue",
            bg="pink",
            font=("Arial", 12, "bold")
        )
        texto.pack(pady=10)

    def mostrar_programa(self):
        # Mantener la ventana abierta
        self.ventana.mainloop()


ventana1 = Programa()

ventana1.iniciar_programa()
ventana1.cargar_texto("Hola como estas")
ventana1.mostrar_programa()