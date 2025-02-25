import tkinter as tk
from tkinter import messagebox
from Database import *
from Persona import *

root = tk.Tk()
root.title("Inicio de Sesión")
root.geometry("300x200")

def abrir_ventana_home(root, usuario_actual):
    ventana_home = tk.Tk()
    ventana_home.title("Home")
    ventana_home.geometry("300x200")

    def cerrar_sesion():
        ventana_home.destroy()

    root.destroy()

    if usuario_actual:
        tk.Label(ventana_home, text=f"Bienvenido {usuario_actual.nombre}").pack()
        tk.Button(ventana_home, text="Cerrar Sesión", command=cerrar_sesion).pack()

def controlador_login():
    global usuario_actual
    correo = entry_correo.get() # daniel@gmail.com
    contraseña = entry_contraseña.get() # 123

    mensaje, usuario = Persona.iniciar_sesion(correo, contraseña, usuarios)

    if usuario:
        usuario_actual = usuario
        abrir_ventana_home(root, usuario_actual)
    else:
        messagebox.showerror("Error", mensaje)

tk.Label(root, text="Login").grid(row=0, column=0, columnspan=2)
entry_correo = tk.Entry(root)
entry_contraseña = tk.Entry(root, show="*")

tk.Label(root, text="Correo: ").grid(row=1, column=0)
entry_correo.grid(row=1, column=1)

tk.Label(root, text="Contraseña: ").grid(row=2, column=0)
entry_contraseña.grid(row=2, column=1)

tk.Button(root, text="Iniciar Sesión", command=controlador_login).grid(row=3, columnspan=2)

root.mainloop()
