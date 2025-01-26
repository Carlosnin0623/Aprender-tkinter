"""
En Tkinter, tanto side como anchor son opciones que se utilizan con el método pack(), pero tienen propósitos distintos y afectan la disposición de los widgets de maneras diferentes.

1. side
Propósito: Define en qué lado del contenedor se colocará el widget.
Valores posibles: "top", "bottom", "left", "right".
Función: Determina la posición principal del widget dentro del contenedor.
Por defecto, side="top", lo que significa que los widgets se apilan verticalmente desde la parte superior del contenedor.
Si se utiliza side="left", los widgets se alinean horizontalmente desde el lado izquierdo, y así sucesivamente.

Ejemplo:
from tkinter import Tk, Button

root = Tk()

btn1 = Button(root, text="Button 1")
btn1.pack(side="left")

btn2 = Button(root, text="Button 2")
btn2.pack(side="right")

root.mainloop()
Aquí, btn1 estará a la izquierda y btn2 a la derecha del contenedor.


Utilidad de anchor

2. anchor
Propósito: Ajusta la alineación del widget dentro del espacio asignado por pack().
Valores posibles: Una combinación de puntos cardinales: "n", "s", "e", "w", "ne", "nw", "se", "sw", y "center".
Función: Indica cómo se posiciona el widget dentro del área disponible. Por ejemplo:
"n": Alineado al norte (parte superior del área).
"center": Centrado dentro del espacio asignado.
"se": Esquina inferior derecha del área.
Ejemplo:

from tkinter import Tk, Button

root = Tk()

btn = Button(root, text="Button")
btn.pack(side="top", anchor="e")  # En el lado superior, alineado a la derecha

root.mainloop()
En este caso, el botón se colocará en la parte superior, pero alineado a la derecha dentro de esa área.

"""

from tkinter import *


ventana = Tk()
ventana.title("Aprendiendo sobre side")
ventana.minsize(600, 400)
ventana.geometry("800x600+350+100")
ventana.maxsize(1024, 768)
ventana.iconbitmap('./imagenes/camara.ico')

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
    bg="black",
    fg="white",
    width=1024,
    pady=20,
    padx=10,
    font=("Arial", 20, "bold")
)
texto.pack()

texto2 = Label(ventana, text="Soy Carlos Nin")
texto2.config(
    bg="orange",
    fg="black",
    height=8,
    width=25,
    font=("Arial", 12, "bold"),
    cursor="arrow"
)
texto2.pack(
    expand=0,
    fill=X
)

texto3 = Label(ventana, text="Basico")
texto3.config(
    bg="green",
    fg="black",
    height=5,
    width=15,
    font=("Arial", 12, "bold")
)
texto3.pack(
    side=LEFT,
    expand=1,
    fill=BOTH
)

texto4 = Label(ventana, text="Basico")
texto4.config(
    bg="red",
    fg="black",
    height=5,
    width=15,
    font=("Arial", 12, "bold")
)
texto4.pack(
    side=LEFT,
    expand=1,
    fill=BOTH
)


texto5 = Label(ventana, text="Basico")
texto5.config(
    bg="orange",
    fg="black",
    height=5,
    width=15,
    font=("Arial", 12, "bold")
)
texto5.pack(
   side=LEFT,
   expand=1,
   fill=BOTH
)


ventana.mainloop()