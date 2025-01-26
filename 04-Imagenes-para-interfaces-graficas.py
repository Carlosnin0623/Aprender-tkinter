from tkinter import *
"""
  Para trabajar con imagenes para nuestras interfaces graficas debemos descargar el modulo pillow.
  debemos instalar esto antes:

  pip install --upgrade pip
  pip install --upgrade Pillow

"""
 
from PIL import Image, ImageTk

from pathlib import Path

import os


ventana = Tk()


ventana.geometry("700x500")

texto = Label(ventana, text="Texto dentro de la ventana")
texto.pack()

# Obteniendo la ruta de la imagen

rutaimagen = str(Path().absolute()) + "/imagenes/logo-gris.jpg"
try:
 if os.path.isfile(rutaimagen):
  mostrarImagenlobo = Image.open(rutaimagen)
  render = ImageTk.PhotoImage(mostrarImagenlobo)
  texto2 = Label(ventana, image=render) # la propiedad image sirve para cargar imagenes desde Tkinter
  texto2.pack()
 else:
   texto2 = Label(ventana, text="La imagen no pudo ser cargada, verificar la ruta de destino....")
   texto2.pack()
   raise ValueError("EL archivo especificado no se encuentra en esta ruta, verificar")
   
except ValueError as error:
  print("Lo siento ha ocurrido un error:" + str(error))



ventana.mainloop()