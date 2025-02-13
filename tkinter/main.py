from tkinter import *
import random

root = Tk()

# root.attributes("-fullscreen", True)

root.title("Nombre de la Aplicación")
root.geometry('350x200')

# LABEL
lbl = Label(root, text = "Hola a todos desde Tkinter",
        fg="white", bg="red", font=("Arial", 15, "bold"))
lbl.pack(expand=True)
# lbl.place(x=100, y=50)

# BUTTON
def accion():
    btn.place(x=random.randint(10, 200), y=random.randint(10, 200))
    lbl.configure(text = "Presionaste el boton")

btn = Button(root, text="Presiona este boton", command=accion)
btn.pack()

root.mainloop()
