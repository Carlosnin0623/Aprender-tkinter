"""
Que es Tkinter: Es un modulo que ya tenemos integrado con python y nos sirve para crear
interfaces graficas.
"""

from tkinter import *


# Crear ventana raíz

ventana = Tk()


# Poner titulo a la ventana

ventana.title("Interfaz grafica con Python y Victor Robles")


# Cambio en el tamaño de la ventana con geometry 750 de ancho y 450 de alto
ventana.geometry("750x450")


# Bloquear el tamaño de la ventana con el metodo resizable si lo pones true podra ampliarse la ventana pero solo en esa direccion

ventana.resizable(False, False)


# como ponerle un logotico a nuestra aplicacion esta imagen debe ser .ico

ventana.iconbitmap('./imagenes/camara.ico')



# Arranca y mostrar la ventana hasta que se cierre

ventana.mainloop()





