"""
Que son los frames: Los frames son marcos que puedes meter dentro de las ventanas
son cajas dentro de nuestra ventana, las cuales podemos modificar o mover por la ventana

para definirlo rapido: son ventanas dentro de otra ventana padre

"""

from tkinter import *


ventana = Tk()

ventana.title("Marcos | Máster en Python")
ventana.geometry("800x600")
ventana.configure(
    bg="white"
)

marco_arriba = Frame(ventana, width=250, height=500)
marco_arriba.config(
    bg="orange",
    bd=2,
    relief="solid",
)
marco_arriba.pack(
    expand=False,
    fill=X
)

"""
 pack_propagate(False) Evita que el marco cambie de tamaño al agregar un texto o cualquier elemento, 
 pero debe ir despues de haber empaquetado el marco osea despues de .pack()

 Es importante no olvidar esto

""" 
marco_arriba.pack_propagate(False)

texto1 = Label(marco_arriba, text="Hola soy un texto")
texto1.config(
  width=40,
  height=10,
  relief="groove"
)
"""

Como centrar un elemento dentro de un frame padre:

para poder centrar un elemento dentro de un frame padre
debemos usar la propiedad expand = True dentro de del pack y automaticamente
lo pondra en el centro, y entonce podemos usar anchor para moveer ese elemento libremente dentro
del contenedor padre

"""

texto1.pack(  
  expand=True,
)


"""

Centrar con place: es un metodo para centrar los elementos mediante coordenadas

Tambien hay otra forma de centrarlo y es usando place en ves de pack

texto1 = Label(marco_arriba, text="Hola soy un texto")
texto1.config(width=20, height=5, relief="groove")

# Centrar el texto dentro del marco
texto1.place(relx=0.5, rely=0.5, anchor="center")

"""

marco_abajo = Frame(ventana, width=250, height=250)
marco_abajo.config(
    bg="white",
    #bd=5, # para crear un borde
    #relief="solid", # PAra definir el tipo de borde
)
marco_abajo.pack(
  side="bottom",
  expand=NO,
  fill=X
)

caja1 = Frame(marco_abajo, width=250, height=250)
caja1.config(
    bg="lightblue",
)
caja1.pack(
    side="left",
    anchor="sw",
    expand=True,
    fill=X
)

caja2 = Frame(marco_abajo, width=250, height=250)
caja2.config(
    bg="pink"
)
caja2.pack(
   anchor="s",
   side="left",
   expand=True,
   fill=X
)

caja3 = Frame(marco_abajo, width=250, height=250)
caja3.config(
    bg="lightgreen"
)
caja3.pack(
    side="right",
    anchor="se",
    expand=True,
    fill=X
)




ventana.mainloop()