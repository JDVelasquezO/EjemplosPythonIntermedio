from tkinter import *

root = Tk()

root.title("Bienvenidos a la Aplicación")
root.geometry('350x200')

lbl = Label(root, text = "Soy un label", fg="blue", bg="yellow", font=("Arial", 12, "bold"))
#Centra label:
lbl.pack(expand=True)
# Posicionar label: lbl.place(x=100, y=50)
# lbl.grid()

def accion():

    res = "Escribiste: " + txt.get()
    lbl.configure(text = res)

btn = Button(root, text = "Hazme click" ,
             fg = "red", command=accion)
btn.pack(side=LEFT)

txt = Entry(root, width=10)
txt.pack()

root.mainloop()
