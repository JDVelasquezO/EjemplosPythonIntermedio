from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.geometry("300x200")

# Funcion booleana
def validaTelefono(text): #
    return text.isdigit() and len(text) <= 8 # True

def validaEmail():
    email = entryEmail.get()
    # correoinventado_158@gmail.com
    # 158correoINVENTADO158@gmail.com
    patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if re.match(patron, email):
        messagebox.showinfo("Exito", "Correo válido")
    else:
        messagebox.showerror("Error", "Correo invalido")



validaNumeros = root.register(validaTelefono)

Label(root, text="Ingresa tu numero:").pack()
entryTel = Entry(root, validate="key", validatecommand=(validaNumeros, "%P")) #1
entryTel.pack()

Label(root, text="Ingresa tu correo:").pack()
entryEmail = Entry(root)
entryEmail.pack()

Button(root, text="Validar Correo", command=validaEmail).pack()

root.mainloop()
