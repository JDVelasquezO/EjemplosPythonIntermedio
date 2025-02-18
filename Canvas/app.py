from tkinter import *

root = Tk()
root.geometry("500x500")

canvas = Canvas(root, width=400, height=400, bg="green")
canvas.pack()

def mover_figura(event):
    canvas.coords(rect, event.x - 50, event.y - 50, event.x + 50, event.y + 50)

rect = canvas.create_rectangle(150, 150, 250, 250, fill="blue")
canvas.bind("<B1-Motion>", mover_figura)

root.mainloop()
