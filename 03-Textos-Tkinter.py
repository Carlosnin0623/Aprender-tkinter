# Importar Tkinter


from tkinter import *



ventana = Tk()

ventana.title("Textos en Tkinter")

ventana.geometry("500x500")

# Parametros de palabras claves ejemplo son utiles ya que podemos usar los parametros para indicar lo que se tiene que ingresar en la funcion

def prueba(nombre, apellido, pais):
    return f"Hola soy {nombre} {apellido} y soy de {pais}"


texto = Label(ventana, text=prueba(nombre="Carlos Alberto", apellido="Nin Queliz", pais="República Dominicana"))
texto.config(
    fg="white", # Estableciendo el color de la letra
    bg="black", # Estableciendo el color de fondo del elemento
    pady=10, # Estableciendo 10 de padding dentro del elementos arriba y abajo
    padx=10, # Estableciendo 10 de padding dentro del elementos derecha y izquierda
    font=("Arial", 10, "bold"), # Estableciendo la fuente de la letra
    width=55, # para establecer la anchura de un elemento
    height=5, # para establecer la altura de un elemento
    anchor=SE, #anchor dentro de config funciona para posicionar el texto dentro del label puede ser a la decha con E, izquierda con W
    cursor="arrow" # representa la apariencia que tomara el mouse al entrar dentro del elemento
)
texto.pack(
    pady=10, # en el metodo pack pady se usa para establecer los margenes de arriba y abajo
    padx=10, # en el metodo pack padx se usa para establecer los margenes de derecha y izquiera
    anchor=CENTER # anchor dentro de pack funciona para posicionar el elemento se quede fijo en una posicion en la ventana
) # El metodo pack permite añadir el elemento se pueda mostrar en el programa

texto2 = Label(ventana, text="Soy Carlos Nin")
texto2.pack()

ventana.mainloop()