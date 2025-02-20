from tkinter import *

def mostrarDatos():
    nombre = entryNombre.get()
    print(f"Nombre ingresado: {nombre}")

def mostrarGenero():
    genero = opcion.get()
    if genero == "M":
        print(f"Género: masculino")
    else:
        print(f"Género: femenino")

def mostrarEstadoCheckbox():
    seleccion = []
    if opcion2.get():
        seleccion.append("Musica")
    if opcion3.get():
        seleccion.append("Teatro")
    if opcion4.get():
        seleccion.append("Cine")

    print(f"Tus gustos son: {seleccion}")

root = Tk()
root.geometry("300x500")
Label(root, text="Escribe tu nombre: ")

entryNombre = Entry(root)
entryNombre.pack()


Button(root, text="Mostrar", command=mostrarDatos).pack()

Label(root, text="Elige el género")
opcion = StringVar(value="F")
Radiobutton(root, text="Masculino", variable=opcion, value="M").pack()
Radiobutton(root, text="Femenino", variable=opcion, value="F").pack()

Button(root, text="Mostrar género", command=mostrarGenero).pack()

Label(root, text="Elige tus gustos:")
opcion2 = IntVar()
opcion3 = IntVar()
opcion4 = IntVar()
Checkbutton(root, text="Musica", variable=opcion2).pack()
Checkbutton(root, text="Teatro", variable=opcion3).pack()
Checkbutton(root, text="Cine", variable=opcion4).pack()

Button(root, text="Mostrar estado", command=mostrarEstadoCheckbox).pack()

root.mainloop()
