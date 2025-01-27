from tkinter import *

ventana = Tk()
ventana.title("Formularios | Master Python")
ventana.geometry("700x400+380+150")
ventana.minsize(500, 200)
ventana.iconbitmap('./imagenes/camara.ico')


# Texto Encabezado 


encabezado = Label(ventana, text="Formularios con Tkinter - Victor Robles")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    pady=10,
    padx=10,
    bd=2,
    relief="solid"
)
encabezado.grid(
  column=0,
  row=0,
  columnspan=12,
  sticky=W, # sticky sirve para pegar los elementos a los bordes de la ventana donde se encuentran
)

# Crear label para pedir nombre

texto_nombre = Label(ventana, text="Escrite tu nombre: ")
texto_nombre.config(
    font=("Open Sans", 12)
)
texto_nombre.grid(
    row=1,
    column=0,
    sticky=W,
    padx=5,
    pady=5
)

# Input para ingresar el nombre 
nombre = Entry(ventana, width=20, font=("Open Sans", 12))
nombre.grid(
    row=1,
    column=1,
    columnspan=6,
    padx=5,
    pady=5
)
nombre.config(
    justify="left",
    state="normal"
)








ventana.mainloop()